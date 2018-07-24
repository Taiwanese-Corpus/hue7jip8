from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class Command(匯入枋模):
    help = 'http://ip194097.ntcu.edu.tw/memory/TGB/thak.asp?id=862'

    公家內容 = {
        '來源': '台灣植物名彙',
        '種類': '字詞',
        '年代': '1928',
    }
    github網址 = (
        'https://github.com/Taiwanese-Corpus/'
        'Syuniti-Sasaki_1928_List-of-Plants-of-Formosa/'
        'raw/master/ChhoeTaigi_TaioanSitbutMialui.csv'
    )

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台文 in self.github資料():
            yield 訓練過渡格式(
                文本=台文,
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def github資料(self):
        with urlopen(self.github網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    羅馬字 = row['poj_unicode'].strip()
                    可能漢字 = row['taigi_hanji'].strip()
                    for lo, han in self.漢羅組合(羅馬字, 可能漢字):
                        try:
                            物件 = 拆文分析器.建立句物件(han, lo)
                        except 解析錯誤 as 錯誤:
                            self.stderr.write(str(錯誤))
                        else:
                            for 字物件 in 物件.篩出字物件():
                                if 字物件.型 == 'XXX':
                                    字物件.型 = 字物件.音
                            yield 物件.看分詞()

    def 漢羅組合(self, 羅馬字, 可能漢字):
        for 漢字 in 可能漢字.replace('？', ' XXX ').split('、'):
            yield 羅馬字, 漢字

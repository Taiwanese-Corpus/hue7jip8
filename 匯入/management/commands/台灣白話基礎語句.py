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
        '來源': '台灣白話基礎語句',
        '種類': '字詞',
        '年代': '1956',
    }
    github網址 = (
        'https://github.com/Taiwanese-Corpus/'
        'Ko-Chek-hoan-Tan-Pang-tin_1956_Basic-Vocabulary-for-Colloquial-Taiwanese/'
        'raw/master/ChhoeTaigi_TaioanPehoeKichhooGiku.csv'
    )

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 羅馬字, 華語 in self.github資料():
            yield 訓練過渡格式(
                    文本=羅馬字,
                    外文=華語,
                    **self.公家內容
                )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def github資料(self):
        with urlopen(self.github網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    羅馬字1 = row['poj_unicode'].strip()
                    羅馬字2 = row['poj_other_unicode'].strip()
                    華語 = row['hoagi'].strip()
                    if 羅馬字2 != '':
                        羅馬字 = [羅馬字1, 羅馬字2]
                    else:
                        羅馬字 = [羅馬字1]
                    for hoa in 華語.split('、'):
                        for lo in 羅馬字:
                            try:
                                台文 = 拆文分析器.建立句物件(lo).看分詞()
                            except 解析錯誤 as 錯誤:
                                print(錯誤)
                            else:
                                yield 台文, 拆文分析器.建立句物件(hoa).看分詞()

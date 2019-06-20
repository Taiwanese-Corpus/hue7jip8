from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'https://github.com/Taiwanese-Corpus/TaiOanUe-LiLiKhokKhok-SuPio'
    資料網址 = 'https://github.com/Taiwanese-Corpus/TaiOanUe-LiLiKhokKhok-SuPio/raw/master/sooji.csv'

    公家內容 = {
        '種類': '字詞',
        '來源': '台語數字',
        '年代': '2019',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台語物件 in self._全部資料():
            yield 訓練過渡格式(
                文本=台語物件.看分詞(),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def _全部資料(self):
        with urlopen(self.資料網址) as tsuliau:
            with io.StringIO(tsuliau.read().decode('utf-8')) as tong:
                for pit in DictReader(tong):
                    yield 拆文分析器.建立句物件(pit['漢字'], pit['羅馬字'])

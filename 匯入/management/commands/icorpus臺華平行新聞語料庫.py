from urllib.request import urlopen

import yaml


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音相容教會羅馬字音標 import 臺灣閩南語羅馬字拼音相容教會羅馬字音標
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'http://icorpus.iis.sinica.edu.tw/'
    yaml網址 = 'https://github.com/sih4sing5hong5/icorpus/raw/master/icorpus.yaml'

    公家內容 = {
        '來源': 'icorpus臺華平行新聞語料庫',
        '種類': '語句',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 一筆 in self._全部資料():
            年代 = 一筆['日期'].split('-')[0]
            for 台語, 華語 in zip(一筆['台語'], 一筆['華語']):
                try:
                    台語物件 = 拆文分析器.建立句物件(台語).轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標)
                    華語物件 = 拆文分析器.建立句物件(華語)
                except 解析錯誤:
                    print(台語, 華語)
                else:
                    yield 訓練過渡格式(
                        文本=台語物件.看分詞(),
                        外文=華語物件.看分詞(),
                        年代=年代,
                        **self.公家內容
                    )

            匯入數量 += 1
            if 匯入數量 % 100 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def _全部資料(self):
        with urlopen(self.yaml網址) as 檔:
            return yaml.load(檔.read().decode())

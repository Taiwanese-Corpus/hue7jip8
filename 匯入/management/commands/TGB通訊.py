from urllib.parse import quote
from urllib.request import urlopen

from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音相容教會羅馬字音標 import 臺灣閩南語羅馬字拼音相容教會羅馬字音標
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class Command(BaseCommand):
    help = '原網站：http://taioanchouhap.pixnet.net/blog。Sîng-hông 2014整理的台華平行版本'
    台文網址 = 'https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/raw/master/語料/TGB/對齊平行閩南語資料'
    華文網址 = 'https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/raw/master/語料/TGB/對齊平行華語資料'

    公家內容 = {
        '來源': 'TGB通訊',
        '種類': '語句',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '--匯入幾筆',
            type=int,
            default=100000,
            help='試驗用，免一擺全匯'
        )

    def handle(self, *args, **參數):
        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

        全部資料 = []
        匯入數量 = 0
        for 台語, 華語 in self._全部資料():
            try:
                台語物件 = 拆文分析器.分詞句物件(台語).轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標)
                華語物件 = 拆文分析器.建立句物件(華語)
            except 解析錯誤 as 錯誤:
                print(台語, 華語, 錯誤)
            else:
                全部資料.append(
                    訓練過渡格式(
                        文本=台語物件.看分詞(),
                        外文=華語物件.看分詞(),
                        年代='2015',
                        **self.公家內容
                    )
                )

            匯入數量 += 1
            if 匯入數量 % 100 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))
            if 匯入數量 == 參數['匯入幾筆']:
                break

        self.stdout.write('檢查格式了匯入')
        訓練過渡格式.加一堆資料(全部資料)

        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

    def _全部資料(self):
        with urlopen(quote(self.台文網址, safe=':/')) as tai:
            with urlopen(quote(self.華文網址, safe=':/')) as hua:
                return zip(
                    tai.read().decode().split('\n'),
                    hua.read().decode().split('\n'),
                )

from csv import DictReader
import io
from urllib.request import urlopen

from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語服務.models import 訓練過渡格式


class Command(BaseCommand):
    help = 'https://github.com/g0v/moedict-data-twblg/'
    例句網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E4%BE%8B%E5%8F%A5.csv'

    公家內容 = {
        '來源': 'icorpus臺華平行新聞語料庫',
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
        年代 = '2018'
        for 台語物件, 華語物件 in self._全部資料():
            全部資料.append(
                訓練過渡格式(
                    文本=台語物件.看分詞(),
                    外文=華語物件.看分詞(),
                    年代=年代,
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

    @classmethod
    def _全部資料(cls):
        with urlopen(cls.例句網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    羅馬字 = row['例句標音'].strip()
                    漢字 = row['例句'].strip()
                    華語翻譯 = row['華語翻譯'].strip()
                    if not 華語翻譯:
                        華語翻譯 = 漢字
                    try:
                        句物件 = (
                            拆文分析器
                            .對齊句物件(漢字, 羅馬字)
                            .轉音(臺灣閩南語羅馬字拼音)
                        )
                    except Exception as 錯誤:
                        print(錯誤)
                        continue
                    華語物件 = 拆文分析器.建立句物件(華語翻譯)
                    yield 句物件, 華語物件

from csv import DictReader
import json

from django.core.management import call_command
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音相容教會羅馬字音標 import 臺灣閩南語羅馬字拼音相容教會羅馬字音標


class Command(BaseCommand):
    公家 = {
        '收錄者': 來源表.objects.get_or_create(名='系統管理員')[0].編號(),
        '來源': 來源表.objects.get_or_create(名='辨識計劃')[0].編號(),
        '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
        '種類': '字詞',
        '語言腔口': '臺語',
        '著作所在地': '臺灣',
        '著作年': '2017',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '常用詞csv',
        )
        parser.add_argument(
            '辭典json',
        )
        parser.add_argument(
            '--匯入幾筆',
            type=int,
            default=10000000,
            help='試驗用，免一擺全匯'
        )

    def handle(self, *args, **參數):
        call_command('顯示資料數量')

        辭典, 外來詞 = self._csv的index(參數['常用詞csv'])
        for 匯入數量, (漢字, 臺羅, 華語) in enumerate(
            self._比較有仝款的無(參數['辭典json'], 辭典, 外來詞)
        ):
            print((漢字, 臺羅, 華語))
#             continue
            外語內容 = {
                '外語語言': '華語',
                '外語資料': 華語,
            }
            外語內容.update(self.公家)
            外語 = 外語表.加資料(外語內容)
            文本內容 = {
                '文本資料': 漢字,
                '音標資料': 臺羅,
            }
            文本內容.update(self.公家)
            外語.翻母語(文本內容)

            if 匯入數量 == 參數['匯入幾筆']:
                break
        call_command('顯示資料數量')

    def _csv的index(self, 常用詞csv所在):
        辭典 = set()
        外來詞 = set()
        with open(常用詞csv所在) as 常用詞csv:
            for 一逝 in DictReader(常用詞csv):
                臺羅 = 一逝['臺羅'].strip()
                數字調 = (
                    拆文分析器
                    .分詞句物件(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
                    .轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標)
                )
                外來詞.add(數字調.看型('-'))
#                 漢字 = 一逝['漢字'].strip()
#                 if 漢字 == 臺羅:
#                     外來詞.add(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
#                 else:
#                     try:
#                         辭典.add(
#                             拆文分析器.對齊句物件(
#                                 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 漢字),
#                                 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
#                             ).看分詞()
#                         )
#                     except:
#                         外來詞.add(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
        return 辭典, 外來詞

    def _比較有仝款的無(self, 辭典json所在, 辭典, 外來詞):
        with open(辭典json所在) as 辭典json:
            for 一條 in json.load(辭典json):
                漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音相容教會羅馬字音標, 一條['臺字'])
                臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音相容教會羅馬字音標, 一條['羅馬'])
                數字調 = (
                    拆文分析器
                    .分詞句物件(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
                    .轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標)
                )
                標準 = 數字調.看型('-')
                if 標準 in 外來詞:
                    yield 漢字, 標準, 一條['華字']
#                 if 漢字 == 臺羅:
#                     if 臺羅 in 外來詞:
#                         yield 漢字, 臺羅, 一條['華字']
#                 else:
#                     print(漢字, 臺羅)
#                     if (
#                         拆文分析器.對齊句物件(漢字, 臺羅).轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標).看分詞()
#                     ) in 辭典:
#                         yield 漢字, 臺羅, 一條['華字']

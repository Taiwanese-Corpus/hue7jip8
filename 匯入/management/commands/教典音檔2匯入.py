from csv import DictReader
from os.path import basename, join, dirname, abspath
from posix import listdir

from django.conf import settings
from django.utils import timezone


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 匯入.指令 import 匯入枋模
from 臺灣言語服務.models import 訓練過渡格式


class Command(匯入枋模):
    公家內容 = {
        '來源': '臺灣閩南語常用詞辭典',
        '影音語者': '王秀容',
        '種類': '字詞',
        '年代': str(timezone.now().year),
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '--匯入幾筆',
            type=int,
            default=100000,
            help='試驗用，免一擺全匯'
        )

    def 全部資料(self, *args, **參數):
        'https://github.com/g0v/moedict-data-twblg/tree/master/uni'
        詞目 = {}
        with open(join(
            dirname(abspath(__file__)), '..', '..',
            '教育部閩南語常用詞辭典', '詞目總檔.csv'
        )) as 檔案:
            for 一筆 in DictReader(檔案):
                編號 = 一筆['主編碼'].strip()
                漢字 = 一筆['詞目'].strip()
                羅馬字 = 一筆['音讀'].strip().split('/')[0]
                try:
                    詞目[int(編號)] = 拆文分析器.對齊組物件(漢字, 羅馬字)
                except 解析錯誤:
                    pass

        音檔目錄 = join(settings.BASE_DIR, '語料', '教育部閩南語常用詞辭典wav')
        匯入數量 = 0
        for 路徑 in sorted(listdir(音檔目錄)):
            音檔路徑 = join(音檔目錄, 路徑)
            if 音檔路徑.endswith('.wav'):
                try:
                    音檔編號 = int(basename(音檔路徑).split('.')[0])
                except ValueError:
                    raise ValueError('有的音檔有重錄過')
                try:
                    台語物件 = 詞目[音檔編號]
                except KeyError:  # 有的詞條尾仔提掉矣，親像編號5
                    continue

                yield 訓練過渡格式(
                    影音所在=音檔路徑,
                    文本=台語物件.看分詞(),
                    **self.公家內容
                )
                匯入數量 += 1
                if 匯入數量 == 參數['匯入幾筆']:
                    break

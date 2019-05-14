from os.path import join, dirname, abspath

from django.conf import settings
from django.core.management.base import BaseCommand


from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '下載方式',
            type=str,
            choices=['dropbox', '官網沓沓掠'],
        )

    def handle(self, *args, **參數):
        專案路徑 = join(
            dirname(abspath(__file__)), '..', '..', '..',
        )
        腳本路徑 = join(
            專案路徑, '匯入', '教育部閩南語常用詞辭典',
            '下載臺語教典音檔-{}.sh'.format(參數['下載方式'])
        )
        語料目錄 = join(
            settings.BASE_DIR, '語料', '教育部閩南語常用詞辭典'
        )
        程式腳本._走指令(['bash', 腳本路徑, 語料目錄], 愛直接顯示輸出=True)

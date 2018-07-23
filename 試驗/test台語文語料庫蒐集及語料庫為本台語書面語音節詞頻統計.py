from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class 教典字詞抑是語句試驗(TestCase):

    def test數量(self):
        call_command('台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計')
        self.assertGreater(訓練過渡格式.資料數量(), 8000)
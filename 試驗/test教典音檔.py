from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class 教典音檔試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('教典音檔0下載', 'dropbox')
        call_command('教典音檔1轉檔', '--匯入幾筆', '100')
        call_command('教典音檔2匯入', '--匯入幾筆', '100')
        return super().setUpClass()

    def test句數正確(self):
        self.assertGreater(訓練過渡格式.資料數量(), 80)

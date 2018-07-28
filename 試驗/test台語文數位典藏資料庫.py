from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class KIPsu試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('台語文數位典藏資料庫')
        return super().setUpClass()

    def test數量(self):
        self.assertGreater(訓練過渡格式.資料數量(), 200000)

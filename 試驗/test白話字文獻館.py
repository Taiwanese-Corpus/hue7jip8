from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class 白話字文獻館試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('白話字文獻館')
        return super().setUpClass()

    def test句數正確(self):
        self.assertGreater(訓練過渡格式.資料數量(), 10000)

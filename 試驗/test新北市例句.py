from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class 新北市例句試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('新北市900例句')
        return super().setUpClass()

    def test句數正確(self):
        self.assertEqual(訓練過渡格式.資料數量(), 300)

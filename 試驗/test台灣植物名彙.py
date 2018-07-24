from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class 台灣植物名彙試驗(TestCase):

    def test句數正確(self):
        call_command('台灣植物名彙')
        self.assertGreater(訓練過渡格式.資料數量(), 600000)

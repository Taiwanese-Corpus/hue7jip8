from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class TGB試驗(TestCase):

    def test句數正確(self):
        call_command('TGB通訊')
        self.assertGreater(訓練過渡格式.資料數量(), 35000)

from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from tempfile import TemporaryFile


class 媠聲試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        with TemporaryFile('wt') as tsiling:
            call_command('SuiSiann', stdout=tsiling, stderr=tsiling)
        return super().setUpClass()

    def test句數正確(self):
        self.assertGreater(訓練過渡格式.資料數量(), 2000)

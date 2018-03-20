from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class 台華雙語試驗(TestCase):

    def test句數正確(self):
        call_command('icorpus臺華平行新聞語料庫')
        self.assertEqual(訓練過渡格式.資料數量(), 83544)

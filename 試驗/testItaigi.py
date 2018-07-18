from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class itaigi試驗(TestCase):

    def test句數正確(self):
        call_command('itaigi')
        self.assertGreater(訓練過渡格式.資料數量(), 8000)

    def test無辭典(self):
        call_command('itaigi')
        self.assertFalse(
            訓練過渡格式.objects.filter(來源__contains='教典').exitsts()
        )
        self.assertFalse(
            訓練過渡格式.objects.filter(來源__contains='台華').exitsts()
        )

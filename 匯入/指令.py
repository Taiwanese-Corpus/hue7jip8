from django.core.management.base import BaseCommand
from 臺灣言語服務.models import 訓練過渡格式


class 匯入枋模(BaseCommand):

    def handle(self, *args, **參數):
        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

        訓練過渡格式.加一堆資料(self.全部資料(*args, **參數))

        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

import io

from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式


class KIPsu試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        with io.StringIO() as tshogoo:
            call_command('教育部臺灣閩南語字詞頻調查工作', stderr=tshogoo)
            print(tshogoo.get_value()[:1000])
        return super().setUpClass()

    def test數量(self):
        self.assertGreater(訓練過渡格式.資料數量(), 50000)

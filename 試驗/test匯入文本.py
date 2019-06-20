from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from setuptools.py31compat import TemporaryDirectory
from os.path import join


class 匯入文本試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        with TemporaryDirectory() as sootsai:
            tongmia = join(sootsai, '資料.txt')
            with open(tongmia, 'w') as tong:
                print('嘛｜mā 好-啦｜hó-lah ，｜,', file=tong)
            call_command('匯入文本', tongmia)
        return super().setUpClass()

    def test文本有確實匯入去(self):
        self.assertEqual(
            訓練過渡格式.objects.get().文本, '嘛｜mā 好-啦｜hó-lah ，｜,'
        )

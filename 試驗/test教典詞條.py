from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.management.commands.教典詞條 import Command


class 教典詞條試驗(TestCase):

    def test句數正確(self):
        call_command('教典詞條')
        self.assertGreater(訓練過渡格式.資料數量(), 25000)

    def test切腔口又音(self):
        self.assertEqual(
            Command().tsheh_iuim('tsa̍p-jī-tsí-tn̂g/tsa̍p-lī-tsí-tn̂g'),
            ['tsa̍p-jī-tsí-tn̂g', 'tsa̍p-lī-tsí-tn̂g']
        )

    def test切tsē又音(self):
        self.assertEqual(
            Command().tsheh_iuim('ē-kì--tsit、ē-kì--lit、ē-kì--lih、ē-kì--eh'),
            ['ē-kì--tsit', 'ē-kì--lit', 'ē-kì--lih', 'ē-kì--eh']
        )

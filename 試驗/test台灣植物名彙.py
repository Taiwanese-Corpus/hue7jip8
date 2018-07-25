from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.management.commands.台灣植物名彙 import Command
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 台灣植物名彙試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('台灣植物名彙')
        super().setUpClass()

    def test句數正確(self):
        self.assertGreater(訓練過渡格式.資料數量(), 1700)

    def test切出一詞(self):
        self.assertEqual(
            list(Command().漢羅組合('Kau-tîn', '鈎藤')),
            [('Kau-tîn', '鈎藤')],
        )

    def test切出兩詞(self):
        self.assertEqual(
            list(Command().漢羅組合('Tsuí-kim-kiann', '水金京、水金驚')),
            [('Tsuí-kim-kiann', '水金京'), ('Tsuí-kim-kiann', '水金驚')],
        )

    def test問號換做XXX(self):
        self.assertEqual(
            list(Command().漢羅組合('Tò-tiàu-hong', '倒？風')),
            [('Tò-tiàu-hong', '倒 XXX 風')],
        )

    def test問號上尾改漢羅(self):
        self.assertTrue(
            訓練過渡格式.objects
            .filter(文本=拆文分析器.建立句物件('倒-tiàu-風', 'Tò-tiàu-hong').看分詞())
            .exists()
        )

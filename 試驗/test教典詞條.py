from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.management.commands.教典詞條 import Command
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 教典詞條試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('教典詞條')
        return super().setUpClass()

    def test句數正確(self):
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

    def test主詞條(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('上青苔', 'tshiūnn-tshenn-thî').看分詞()
            ).exists()
        )

    def test第二優勢腔(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('上青苔', 'tshiūnn-tshinn-thî').看分詞()
            ).exists()
        )

    def test又音(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('上青苔', 'tshiūnn-tshenn-tî').看分詞()
            ).exists()
        )

    def test詞luī方言差(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('面巾', 'bīn-kirn').看分詞()
            ).exists()
        )

    def test詞luī方言差2ê做伙(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('病院', 'pǐnn-ǐnn').看分詞()
            ).exists()
        )

    def test詞luī方言差日語莫(self):
        self.assertFalse(
            訓練過渡格式.objects.filter(
                文本__contains='にんじん'
            ).exists()
        )

from unittest.case import skip

from django.core.management import call_command
from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 台語數字試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('台語數字')
        return super().setUpClass()

    def test11到99(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('六十七', 'la̍k-tsa̍p-tshit').看分詞()
            ).exists()
        )

    def test幾外thóng(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('百外', 'pah-guā').看分詞()
            ).exists()
        )

    @skip
    def test數詞幾外thóng(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('三萬捅', 'sann-bān-thóng').看分詞()
            ).exists()
        )

    def test單位(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('七億', 'tshit-ik').看分詞()
            ).exists()
        )

    def test單位kap數詞(self):
        self.assertTrue(
            訓練過渡格式.objects.filter(
                文本=拆文分析器.建立句物件('千五', 'tshing-gōo').看分詞()
            ).exists()
        )

from django.test.testcases import TestCase
from 匯入.教典 import 字詞抑是語句
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 教典字詞抑是語句試驗(TestCase):

    def test字詞(self):
        self.assertEqual(
            字詞抑是語句(拆文分析器.建立句物件('一蕊花', 'tsi̍t luí hue')),
            '字詞'
        )

    def test語句(self):
        self.assertEqual(
            字詞抑是語句(
                拆文分析器.建立句物件(
                    '紅嬰仔哭甲一身軀汗。',
                    'Âng-enn-á khàu kah tsi̍t sin-khu kuānn.'
                )
            ),
            '語句'
        )

from django.test.testcases import TestCase
from 匯入.教典 import 字詞抑是語句


class 教典字詞抑是語句試驗(TestCase):

    def test字詞(self):
        self.assertEqual(
            字詞抑是語句('一蕊花', 'tsi̍t luí hue'),
            '字詞'
        )

    def test語句(self):
        self.assertEqual(
            字詞抑是語句('紅嬰仔哭甲一身軀汗。', 'Âng-enn-á khàu kah tsi̍t sin-khu kuānn.'),
            '語句'
        )

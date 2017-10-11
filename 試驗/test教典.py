from django.test.testcases import TestCase
from 匯入到臺灣言語資料庫.教育部閩南語常用詞辭典.教典 import 教典


class 教典試驗(TestCase):

    def setUp(self):
        self.一月日詞目 = {
            '主編碼': '6',
            '屬性': '1',
            '詞目': '一月日',
            '音讀': 'tsi̍t gue̍h-ji̍t/tsi̍t ge̍h-li̍t',
            '文白屬性': '0',
            '部首': '',
        }
        self.一日月華語 = {
            'kokgi_no': '9',
            'n_no': '6',
            'kokgi': '一個月',
            'kokgi_v': '一個月',
        }
        self.一教典 = 教典()

    def test下載詞目正確(self):
        詞目總檔陣列 = self.一教典.下載詞目總檔()
        self.assertEqual(詞目總檔陣列[4], self.一月日詞目)

    def test下載華語正確(self):
        華語檔陣列 = self.一教典.下載對應華語檔()
        self.assertEqual(華語檔陣列[8], self.一日月華語)

    def test取得臺羅對照華語(self):
        臺羅華陣列 = self.一教典.取得臺羅對照華語()
        是否有一日月 = False
        for 一物件 in 臺羅華陣列:
            if 一物件['臺字'] == '一日月':
                是否有一日月 = True
                self.assertEqual(一物件, {
                    '臺字': '一月日',
                    '羅馬': 'tsit8 gueh8-jit8',
                    '華字': '一個月',
                })
        self.assertTrue(是否有一日月)

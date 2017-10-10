from django.test.testcases import TestCase
from 匯入到臺灣言語資料庫.教育部閩南語常用詞辭典.教典 import 教典


class 教典試驗(TestCase):

    def setUp(self):
        self.詞目一月日 = {
            '主編碼': '6',
            '屬性': '1',
            '詞目': '一月日',
            '音讀': 'tsi̍t gue̍h-ji̍t/tsi̍t ge̍h-li̍t',
            '文白屬性': '0',
            '部首': '',
        }

    def test下載資料正確(self):
        一教典 = 教典()
        詞目總檔陣列 = 一教典.下載詞目總檔()
        self.assertEqual(詞目總檔陣列[4], self.詞目一月日)

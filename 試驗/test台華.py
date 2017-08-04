from django.test.testcases import TestCase
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語資料庫.資料模型 import 文本表
from 匯入到臺灣言語資料庫.台華辭典 import 下載
from 匯入到臺灣言語資料庫.台華辭典 import 匯入一筆

# 測試：
# 台華下載
# 台華匯入


class 台華試驗(TestCase):

    def setUp(self):
        self.下載資料阿母 = {
            'ID': '12',
            '台語羅馬字': 'a-bo2',
            '台語羅馬字2': 'a-bu2',
            '台語漢字': '阿母',
            '華語對譯': ';母親;媽媽;',
            '英文': 'mother',
            'freq': '1884',
            'pos_h': 'Na'
        }
        self.下載資料鬱熱 = {
            'ID': '62024',
            '台語羅馬字': 'ut-joah8',
            '台語羅馬字2': '',
            '台語漢字': '鬱熱',
            '華語對譯': ';悶熱;',
            '英文': '',
            'freq': '536',
            'pos_h': 'VH'
        }

    def test下載詞目數正確(self):
        台華辭典陣列 = 下載()
        self.assertEqual(len(台華辭典陣列), 62045)

    def test下載資料正確(self):
        台華辭典陣列 = 下載()
        self.assertEqual(台華辭典陣列[11], self.下載資料阿母)

    def test匯入外語數量正確(self):
        # '華語對譯': ';母親;媽媽;',
        # '英文': 'mother',
        匯入一筆(self.下載資料阿母)
        self.assertEqual(外語表.objects.count(), 3)

    def test匯入外語英文正確(self):
        匯入一筆(self.下載資料阿母)
        一外語 = 外語表.objects.get(外語資料='mother')
        self.assertEqual(一外語.外語語言.語言腔口, '英語') 

    def test匯入外語華語正確(self):
        匯入一筆(self.下載資料阿母)
        一外語 = 外語表.objects.get(外語資料='母親')
        外語表.objects.get(外語資料='媽媽')
        self.assertEqual(一外語.外語語言.語言腔口, '華語') 

    def test匯入文本數量正確(self):
        匯入一筆(self.下載資料阿母)
        self.assertEqual(文本表.objects.count(), 6)

    def test匯入文本翻譯文本數量正確(self):
        匯入一筆(self.下載資料阿母)
        一外語 = 外語表.objects.get(外語資料='母親')
        self.assertEqual(一外語.翻譯文本.count(), 2)

    def test匯入教羅轉臺羅(self):
        # 62024, ut-joah8 -> ut-juah8
        匯入一筆(self.下載資料鬱熱)
        一文本 = 文本表.objects.get(文本資料='鬱熱')
        self.assertEqual(一文本.音標資料, 'ut4-juah8')

    def test匯入外語詞性(self):
        匯入一筆(self.下載資料阿母)
        一外語 = 外語表.objects.get(外語資料='母親')
        self.assertEqual(一外語.屬性內容(), {'詞性': 'Na'})

    def test匯入文本不要有詞性(self):
        匯入一筆(self.下載資料鬱熱)
        一文本 = 文本表.objects.get(文本資料='鬱熱')
        self.assertEqual(一文本.屬性內容(), {})

from django.conf import settings
from os.path import join
from os import makedirs
from urllib.request import urlopen
import io
from csv import DictReader
# from 匯入到臺灣言語資料庫.台華辭典 import 處理音標


class 教典():
    對應華語檔 = ('https://raw.githubusercontent.com/g0v/' +
             'moedict-data-twblg/master/uni/' +
             '%E5%B0%8D%E6%87%89%E8%8F%AF%E8%AA%9E.csv')
    詞目總檔 = ('https://raw.githubusercontent.com/g0v/' +
            'moedict-data-twblg/master/uni/' +
            '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv')

    def 下載對應華語檔(self):
        return self.下載(self.對應華語檔)

    def 下載詞目總檔(self):
        return self.下載(self.詞目總檔)
        
    def 下載(self, 下載網址):
        print('下載', 下載網址)
        語料目錄 = join(settings.BASE_DIR, '語料', '教典')
        makedirs(語料目錄, exist_ok=True)
        with urlopen(下載網址) as 資料檔案:
            全部資料csv = 資料檔案.read().decode('utf-8')
            with io.StringIO(全部資料csv) as 詞目:
                讀檔 = DictReader(詞目)
                輸出陣列 = []
                for 一逝 in 讀檔:
                    輸出陣列.append(一逝)
#                 print('輸出', 輸出陣列)
                return 輸出陣列

    def 列印詞目總檔(self, 陣列):
        for 一筆 in 陣列:
            self.列印一筆詞目(一筆)
        return

    def 列印一筆詞目(self, 一筆):
        # 主編碼,屬性,詞目,音讀,文白屬性,部首
        # 1,1,一,tsi̍t/tsi̍t,4,一
        台語漢字 = 一筆['詞目'].strip()
        for 臺羅 in 一筆['台語羅馬字'].strip().split('/'):
            self.列印一筆辭典(音標, 台語漢字, 華語)
        return

    def 列印一筆辭典(self, 音標陣列, 台語漢字, 外語字):
        for 臺羅音標 in 音標陣列:
            print('{} {} {}'.format(台語漢字, 臺羅音標, 外語字))

    def 處理音標(self, 音標):
        return (
            拆文分析器
            .建立句物件(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音相容教會羅馬字音標, 音標))
            .轉音(臺灣閩南語羅馬字拼音相容教會羅馬字音標)
            .看型(物件分字符號=分字符號, 物件分詞符號=分詞符號)
        )
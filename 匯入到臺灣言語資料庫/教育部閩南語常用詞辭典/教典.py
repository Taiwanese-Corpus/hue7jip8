from django.conf import settings
from os.path import join
from os import makedirs
from urllib.request import urlopen
import io
from csv import DictReader
from urllib.parse import unquote
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
                return 輸出陣列

    def 取得臺羅對照華語(self):
        對應華語檔 = self.下載對應華語檔()
        詞目總檔 = self.下載詞目總檔()
        臺羅華結果 = [] 
        
        for 一詞目 in 詞目總檔:
            # 一字多音分成兩個詞
#             print('一詞目', 一詞目)
            臺字 = 一詞目['詞目'].strip()
            臺編號 = 一詞目['主編碼'].strip()
            for 一羅馬 in 一詞目['音讀'].strip().split('/'):
                for 一逝 in 對應華語檔:
                    if 一逝['n_no'] == 臺編號:
#                         print('一逝', 臺編號, 臺字, 一逝)
                        華字 = 一逝['kokgi']
                        臺羅華結果.append({
                            '臺字': 臺字,
                            '羅馬': 一羅馬,
                            '華字': 華字,
                        })
#             if 臺字 == '一月日':
#                 return
        return 臺羅華結果

from django.conf import settings
from os.path import join
from os import makedirs
from urllib.request import urlopen
import io
from csv import DictReader


class 教典():
    對應華語檔 = ('https://raw.githubusercontent.com/g0v/'+
             'moedict-data-twblg/master/uni/'+
             '%E5%B0%8D%E6%87%89%E8%8F%AF%E8%AA%9E.csv')
    
    def 下載對應華語檔(self):
        self.下載(self.對應華語檔)

    def 下載(self, 下載名稱):
        語料目錄 = join(settings.BASE_DIR, '語料', '教典')
        makedirs(語料目錄, exist_ok=True)
        with urlopen(下載名稱) as 資料檔案:
            全部資料csv = 資料檔案.read().decode('utf-8')
            with io.StringIO(全部資料csv) as 詞目:
                讀檔 = DictReader(詞目)
                輸出陣列 = []
                for 一逝 in 讀檔:
                    輸出陣列.append(一逝)
                return 輸出陣列
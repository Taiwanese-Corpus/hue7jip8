from django.conf import settings
from os.path import join
from os import makedirs
from urllib.request import urlopen
import io
from csv import DictReader


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
        華語迴圈索引 = 0
        for 一詞目 in 詞目總檔:
            # 一臺多華分成多個詞
            # 多臺一華分成多個詞
            臺字 = 一詞目['詞目'].strip()
            臺編號 = 一詞目['主編碼'].strip()
            for 索引, 一逝 in enumerate(對應華語檔[華語迴圈索引:], start=華語迴圈索引):
                if 一逝['n_no'] == 臺編號:
                    華字 = 一逝['kokgi']
                    for 一羅馬 in 一詞目['音讀'].strip().split('/'):
                        臺羅華結果.append({
                            '臺字': 臺字,
                            '羅馬': 一羅馬,
                            '華字': 華字,
                        })
                else:
                    華語迴圈索引 = 索引
                    break
        return 臺羅華結果

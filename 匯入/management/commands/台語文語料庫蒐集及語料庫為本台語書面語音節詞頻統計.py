from csv import DictReader
import io
from os import walk
from os.path import join, basename, dirname
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZipFile


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.教典 import 字詞抑是語句
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'http://ip194097.ntcu.edu.tw/giankiu/keoe/KKH/guliau-supin/guliau-supin.asp'
    zip網址 = 'https://github.com/Taiwanese-Corpus/Ungian_2005_guliau-supin/archive/master.zip'

    來源 = '台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計',
    公家內容 = {
        '年代': '2005',
    }
    欄位表 = {
        'luipiat': '類別',
        'chokchia': '作者',
        'piautoe': '標題',
        'tongmia': '檔名',
        'nitai': '年代',
        'lamlu': '男女',
    }
    性別表 = {'b': '查某', 'p': '查甫', 'm': '毋知'}

    def 全部資料(self, *args, **參數):
        全部資料 = []
        匯入數量 = 0
        for 資料 in self._全部資料():
            print(
                    資料,
                    )
            全部資料.append(
                訓練過渡格式(
                    **資料,
                    **self.公家內容
                )
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

        return 全部資料

    def _全部資料(self):
        with TemporaryDirectory() as 資料夾:
            with urlopen(self.zip網址) as 網路檔:
                with io.BytesIO(網路檔.read()) as 檔:
                    with ZipFile(檔) as 資料:
                        資料.extractall(資料夾)
            yield from self.轉規類(join(資料夾, '轉換後資料'), 'HL')
            yield from self.轉規類(join(資料夾, '轉換後資料'), 'POJ')

    def 轉規類(self, 語料資料夾, 類):
        目錄 = {}
        with open(join(語料資料夾, '{}.csv'.format(類))) as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                資料 = {}
                for 欄位, 內容 in row.items():
                    try:
                        資料[self.欄位表[欄位]] = 內容
                    except:
                        pass
                資料['男女'] = self.性別表[資料['男女']]
                檔名 = 資料.pop('檔名')
                目錄[檔名] = 資料
        for 所在, _資料夾, 檔名陣列 in walk(join(語料資料夾, 類)):
            for 檔名 in 檔名陣列:
                with open(join(所在, 檔名)) as 檔:
                    try:
                        來源內容 = 目錄.pop(檔名[:-4])
                    except:
                        作者 = basename(所在)
                        類別 = basename(dirname(所在))
                        來源內容 = {'作者': 作者, '類別': 類別}

                    for 一逝 in 檔.readlines():
                        文本資料 = 一逝.strip()
                        print(一逝)
                        if len(文本資料) > 0:
                            資料 = {
                                '來源': '{}-{}-{}-{}'.format(
                                    self.來源, 類, 來源內容['作者'], 來源內容['類別']
                                ),
                                '文本': 文本資料,
                            }
                            yield 資料
        if len(目錄) > 0:
            print('目錄賰：', 目錄.keys(), self.stderr)
            raise RuntimeError('表有物件無對著！！')

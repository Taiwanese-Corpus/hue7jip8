import io
import json
from os import walk
from os.path import join
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZipFile


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class Command(匯入枋模):
    help = 'http://ip194097.ntcu.edu.tw/Ungian/Chokphin/Lunbun/KIPsupin/KIPsupin.asp'
    zip網址 = 'https://github.com/Taiwanese-Corpus/Ungian_2009_KIPsupin/archive/master.zip'

    公家內容 = {
        '來源': '教育部臺灣閩南語字詞頻調查工作',
        '年代': '2009',
        '種類': '語句',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台文 in self._全部資料():
            yield 訓練過渡格式(
                文本=台文.看分詞(),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def _全部資料(self):
        with TemporaryDirectory() as 資料夾:
            with urlopen(self.zip網址) as 網路檔:
                with io.BytesIO(網路檔.read()) as 檔:
                    with ZipFile(檔) as 資料:
                        資料.extractall(資料夾)
            yield from self.規目錄(
                join(資料夾, 'Ungian_2009_KIPsupin-master/', 'JSON格式資料')
            )

    def 規目錄(self, 語料資料夾):
        for 所在, _資料夾, 檔名陣列 in sorted(walk(語料資料夾)):
            for 檔名 in 檔名陣列:
                with open(join(所在, 檔名)) as 檔:
                    一檔 = json.load(檔)
                for 一篇 in 一檔['資料']:
                    一段 = 一篇['段']
                    for 漢羅, 羅 in 一段:
                        yield from self.轉物件(漢羅, 羅)

    def 轉物件(self, 漢羅, 羅):
        try:
            yield 拆文分析器.建立句物件(漢羅, 羅)
            return
        except 解析錯誤 as 錯誤:
            print(錯誤, file=self.stderr)
        try:
            yield 拆文分析器.建立句物件(羅)
            return
        except 解析錯誤 as 錯誤:
            print(錯誤, file=self.stderr)

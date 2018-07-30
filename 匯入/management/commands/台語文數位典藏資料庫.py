import io
import json
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class Command(匯入枋模):
    help = 'http://xdcm.nmtl.gov.tw/dadwt/pbk.asp'
    json網址 = (
        'https://github.com/Taiwanese-Corpus/nmtl_2006_dadwt/'
        'raw/master/nmtl.json'
    )

    公家內容 = {
        '來源': '台語文數位典藏資料庫',
        '年代': '2006',
        '種類': '語句',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '--錯誤印部份就好',
            action='store_true',
            help='因為CI有限制輸出4M',
        )

    def 全部資料(self, *args, **參數):
        self.錯誤全印 = not 參數['錯誤印部份就好']

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
        for 漢羅, 羅 in self._全部漢羅():
            try:
                yield from self.轉物件(漢羅, 羅)
            except ValueError:
                'https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/issues/566'
                pass

    def _全部漢羅(self):
        with urlopen(self.json網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料json:
                for phinn in json.load(資料json):
                    yield phinn['漢羅名'], phinn['全羅名']
                    yield phinn['漢羅標'], phinn['全羅標']
                    yield from phinn['資料']

    def 轉物件(self, 漢羅, 羅):
        try:
            yield 拆文分析器.建立句物件(漢羅, 羅)
            return
        except 解析錯誤 as 錯誤:
            if self.錯誤全印:
                self.stderr.write(錯誤)
            else:
                self.stderr.write(str(錯誤)[:40])
        try:
            yield 拆文分析器.建立句物件(羅)
            return
        except 解析錯誤 as 錯誤:
            if self.錯誤全印:
                self.stderr.write(錯誤)
            else:
                self.stderr.write(str(錯誤)[:40])

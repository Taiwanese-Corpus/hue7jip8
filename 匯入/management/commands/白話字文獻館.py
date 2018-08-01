import io
import json
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'pojbh.lib.ntnu.edu.tw'
    json網址 = (
        'https://github.com/Taiwanese-Corpus/Khin-hoan_2010_pojbh/'
        'raw/master/pojbh.json'
    )

    公家內容 = {
        '來源': '白話字文獻館',
        '種類': '語句',
        '年代': '2010',
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
        for 台語物件 in self._全部資料():
            yield 訓練過渡格式(
                文本=台語物件.看分詞(),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 條'.format(匯入數量))

    def _全部資料(self):
        with urlopen(self.json網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for phinn in json.load(資料):
                    if len(phinn['tailo']) != len(phinn['hanlo']):
                        for tuann in phinn['tailo']:
                            yield from self.羅轉物件(tuann)
                    else:
                        for han, lo in zip(phinn['hanlo'], phinn['tailo']):
                            yield from self.轉物件(han, lo)

    def 轉物件(self, 漢羅, 羅):
        try:
            try:
                yield 拆文分析器.建立句物件(漢羅, 羅)
            except ValueError:
                'https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/issues/566'
                raise 解析錯誤(ValueError)
        except 解析錯誤 as 錯誤:
            if self.錯誤全印:
                self.stderr.write(錯誤)
            else:
                self.stderr.write(str(錯誤)[:40])
            yield from self.羅轉物件(羅)

    def 羅轉物件(self, 羅):
        try:
            yield 拆文分析器.建立句物件(羅)
        except 解析錯誤 as 錯誤:
            if self.錯誤全印:
                self.stderr.write(錯誤)
            else:
                self.stderr.write(str(錯誤)[:40])

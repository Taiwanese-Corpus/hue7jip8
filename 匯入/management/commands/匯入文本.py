from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模
from django.utils.timezone import now
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class Command(匯入枋模):
    公家內容 = {
        '種類': '語句',
    }

    def add_arguments(self, parser):
        parser.add_argument('檔名')

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台語物件 in self._全部資料(參數['檔名']):
            yield 訓練過渡格式(
                文本=台語物件.看分詞(),
                年代=now().year,
                來源=參數['檔名'],
                **self.公家內容
            )
            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def _全部資料(self, 檔名):
        with open(檔名) as tong:
            for tsua in tong:
                yield 拆文分析器.分詞句物件(tsua.rstrip())

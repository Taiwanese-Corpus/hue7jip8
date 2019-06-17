from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.教典 import 字詞抑是語句
from 匯入.指令 import 匯入枋模
from json.decoder import _decode_uXXXX
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字


class Command(匯入枋模):
    help = 'https://github.com/g0v/moedict-data-twblg/'
    例句網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E4%BE%8B%E5%8F%A5.csv'

    公家內容 = {
        '種類':'字詞',
        '來源': '台語數字',
        '年代': '2019',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台語物件 in self._全部資料():
            yield 訓練過渡格式(
                文本=台語物件.看分詞(),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))
    def _全部資料(self):
        a = []
        for sooji in range(11,100):
            a.append(阿拉伯數字().轉數量('空', str(sooji)))
        print(a)
#         return [
#             拆文分析器.建立句物件('百外', 'pah-guā'),
#             拆文分析器.建立句物件('百sann', 'pah-sann'),
#             ]
        
        yield 拆文分析器.建立句物件(a,'pah-guā')
        yield 拆文分析器.建立句物件('百sann', 'pah-sann')
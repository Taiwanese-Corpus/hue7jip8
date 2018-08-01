from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.教典 import 字詞抑是語句
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'https://github.com/g0v/moedict-data-twblg/'
    例句網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E4%BE%8B%E5%8F%A5.csv'

    公家內容 = {
        '來源': '教典例句',
        '年代': '2018',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 台語物件, 華語物件 in self._全部資料():
            yield 訓練過渡格式(
                文本=台語物件.看分詞(),
                外文=華語物件.看分詞(),
                種類=字詞抑是語句(台語物件),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    @classmethod
    def _全部資料(cls):
        with urlopen(cls.例句網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    羅馬字 = row['例句標音'].strip()
                    漢字 = row['例句'].strip()
                    華語翻譯 = row['華語翻譯'].strip()
                    if not 華語翻譯:
                        華語翻譯 = 漢字
                    try:
                        句物件 = (
                            拆文分析器
                            .對齊句物件(漢字, 羅馬字)
                            .轉音(臺灣閩南語羅馬字拼音)
                        )
                    except Exception as 錯誤:
                        print(row)
                        print(錯誤)
                        continue
                    華語物件 = 拆文分析器.建立句物件(華語翻譯)
                    yield 句物件, 華語物件

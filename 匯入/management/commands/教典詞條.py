from csv import DictReader
import io
from itertools import chain
import re
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 匯入.教典 import 字詞抑是語句
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'https://github.com/g0v/moedict-data-twblg/。詞條kah又見音'

    公家內容 = {
        '來源': '教典詞條',
        '年代': '2018',
    }
    github網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/'
    詞目總檔網址 = (
        github網址 + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    )
    詞目總檔屬性網址 = (
        github網址 +
        '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94'
        '.%E8%A9%9E%E7%9B%AE%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    )
    又音網址 = (
        github網址 + '%E5%8F%88%E9%9F%B3.csv'
    )
    例句網址 = (
        github網址 + '%E4%BE%8B%E5%8F%A5.csv'
    )

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 漢字, 羅馬字 in chain(self.詞目總檔(), self.又見音表()):
            try:
                if 羅馬字 != '':
                    句物件 = 拆文分析器.建立句物件(漢字, 羅馬字)
                else:
                    句物件 = 拆文分析器.建立句物件(漢字)
            except Exception as 錯誤:
                print(錯誤)
                continue
            yield 訓練過渡格式(
                文本=句物件.看分詞(),
                種類=字詞抑是語句(句物件),
                **self.公家內容
            )

            匯入數量 += 1
            if 匯入數量 % 5000 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))

    def 詞目總檔(self):
        會使的屬性 = set()
        with urlopen(self.詞目總檔屬性網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    屬性 = row['屬性'].strip()
                    if (
                        '地名' not in 屬性 and
                        '外來詞表' not in 屬性
                    ):
                        會使的屬性.add(row['編號'].strip())
        with urlopen(self.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    if row['屬性'].strip() not in 會使的屬性:
                        continue
                    音讀 = row['音讀'].strip()
                    漢字 = row['詞目'].strip()
                    for 一音 in self.tsheh_iuim(音讀):
                        臺羅 = 一音.strip()
                        yield 漢字, 臺羅

    def 又見音表(self):
        資料 = {}
        with urlopen(self.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    主編碼 = row['主編碼'].strip()
                    漢字 = row['詞目'].strip()
                    資料[主編碼] = 漢字

        with urlopen(self.又音網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    if row['又音類型(1.又唸作 2.俗唸作 3.合音唸作)'] == '3':
                        continue
                    主編碼 = row['主編碼'].strip()
                    漢字 = 資料[主編碼]
                    for 一音 in self.tsheh_iuim(row['又音']):
                        臺羅 = 一音.strip()
                        yield 漢字, 臺羅

    _tsheh = re.compile('[、/]')

    def tsheh_iuim(self, iuim):
        return self._tsheh.split(iuim)

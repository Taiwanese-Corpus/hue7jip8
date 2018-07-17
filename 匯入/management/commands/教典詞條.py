from csv import DictReader
import io
from urllib.request import urlopen

from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語服務.models import 訓練過渡格式


class Command(BaseCommand):
    help = 'https://github.com/g0v/moedict-data-twblg/'
    詞目總檔網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    詞目總檔屬性網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    又音網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E5%8F%88%E9%9F%B3.csv'
    例句網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E4%BE%8B%E5%8F%A5.csv'

    @classmethod
    def 全部資料(cls):
        yield from cls.詞目總檔()
        yield from cls.又見音表()
        yield from cls.例句()

    公家內容 = {
        '來源': '教典例句',
        '種類': '語句',
    }


    def handle(self, *args, **參數):
        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

        全部資料 = []
        匯入數量 = 0
        年代 = '2018'
        for 台語物件, 華語物件 in self._全部資料():
            全部資料.append(
                訓練過渡格式(
                    文本=台語物件.看分詞(),
                    外文=華語物件.看分詞(),
                    年代=年代,
                    **self.公家內容
                )
            )

            匯入數量 += 1
            if 匯入數量 % 100 == 0:
                self.stdout.write('匯入 {} 筆'.format(匯入數量))
          
        self.stdout.write('檢查格式了匯入')
        訓練過渡格式.加一堆資料(全部資料)

        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))

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

    def 詞目總檔(self):
        會使的屬性 = set()
        with urlopen(self.詞目總檔屬性網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    if '地名' not in row['屬性'].strip():
                        會使的屬性.add(row['編號'].strip())
        with urlopen(self.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    音讀 = row['音讀'].strip()
                    if 音讀 == '' or row['屬性'].strip() not in 會使的屬性:
                        continue
                    漢字 = row['詞目'].strip()
                    for 一音 in 音讀.split('/'):
                        臺羅 = 一音.strip()
                        整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 漢字)
                        整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(整理後漢字, 整理後臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)
    def 又見音表(self):
        資料 = {}
        with urlopen(self.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    主編碼 = row['主編碼'].strip()
                    漢字 = row['詞目'].strip()
                    音讀 = row['音讀'].split('/')[0].strip()
                    資料[主編碼] = (漢字, 音讀)

        with urlopen(cls.又音網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    if row['又音類型(1.又唸作 2.俗唸作 3.合音唸作)'] == '3':
                        continue
                    主編碼 = row['主編碼'].strip()
                    (優勢腔漢字, _優勢腔音讀) = 資料[主編碼]
                    優勢腔整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 優勢腔漢字)
                    for 一音 in row['又音'].split('/'):
                        臺羅 = 一音.strip()
                        整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(優勢腔整理後漢字, 整理後臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)

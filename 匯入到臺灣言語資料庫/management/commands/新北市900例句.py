from os import makedirs
from os.path import join, isfile
from posix import listdir
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve
from zipfile import ZipFile

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from libavwrapper.avconv import Input, Output, AVConv
from libavwrapper.codec import AudioCodec, NO_VIDEO


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語資料庫.資料模型 import 影音表


class Command(BaseCommand):
    help = 'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3'

    公家內容 = {
        '收錄者': 來源表.objects.get_or_create(名='系統管理員')[0].編號(),
        '來源': (
            來源表.objects
            .get_or_create(名='新北市104學年度閩南語字音字形-臺語上美麗辭典揣舉例-900例句工作坊')[0]
            .編號()
        ),
        '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
        '種類': '字詞',
        '語言腔口': '臺語',
        '著作所在地': '臺灣',
        '著作年': '2015',
        '屬性': {'語者': '王秀容'}
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '--頻率',
            type=int,
            default=44100,
        )
        parser.add_argument(
            '--匯入幾筆',
            type=int,
            default=100000,
            help='試驗用，免一擺全匯'
        )

    def handle(self, *args, **參數):
        call_command('顯示資料數量')

        網址 = 'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3/archive/master.zip'
        語料目錄 = join(settings.BASE_DIR, '語料', '新北市900例句')
        makedirs(語料目錄, exist_ok=True)
        暫時檔案 = join(語料目錄, 'master.zip')
        if not isfile(暫時檔案):
            urlretrieve(網址, 暫時檔案)
        ZipFile(暫時檔案).extractall(語料目錄)
        匯入數量 = 0
        with TemporaryDirectory() as 轉檔目錄:
            音檔目錄 = join(
                語料目錄, 'Sin1pak8tshi7_2015_900-le7ku3-master', '鉸好的1-150音檔'
            )
            音檔陣列 = []
            for 檔名 in sorted(listdir(音檔目錄), key=lambda 名: int(名.split('.')[0])):
                來源 = join(音檔目錄, 檔名)
                目標 = join(轉檔目錄, 檔名)
                目標聲音格式 = (
                    AudioCodec('pcm_s16le')
                    .channels(1)
                    .frequence(參數['頻率'])
                )
                原始檔案 = Input(來源)
                網頁檔案 = Output(目標).overwrite()
                指令 = AVConv('avconv', 原始檔案, 目標聲音格式, NO_VIDEO, 網頁檔案)
                指令.run().wait()
                音檔陣列.append(目標)
            with open(
                join(語料目錄, 'Sin1pak8tshi7_2015_900-le7ku3-master', 'minnan900.分詞')
            ) as 分詞檔案:
                for 一逝分詞, 音檔路徑 in zip(分詞檔案.readlines(), 音檔陣列):
                    章物件 = 拆文分析器.分詞章物件(一逝分詞.strip())
                    影音內容 = {'影音所在': 音檔路徑}
                    影音內容.update(self.公家內容)
                    影音 = 影音表.加資料(影音內容)
                    文本內容 = {
                        '文本資料': 章物件.看型(),
                        '音標資料': 章物件.看音(),
                    }
                    文本內容.update(self.公家內容)
                    影音.寫文本(文本內容)

                    匯入數量 += 1
                    if 匯入數量 == 參數['匯入幾筆']:
                        break
        call_command('顯示資料數量')

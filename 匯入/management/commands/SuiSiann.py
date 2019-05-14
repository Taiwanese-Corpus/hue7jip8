from os import makedirs
from os.path import join, isfile
from posix import listdir
from subprocess import run

from django.conf import settings


from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模
from csv import DictReader
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from tarfile import TarFile


class Command(匯入枋模):
    help = 'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3'

    公家內容 = {
        '來源': '臺灣媠聲2.0',
        '影音語者': '王秀容',
        '種類': '語句',
        '年代': '2019',
    }

    網址 = 'https://www.dropbox.com/s/gxu3vzspeo2x1p6/SuiSiann-0.1.tar?dl=0'

    def add_arguments(self, parser):
        parser.add_argument(
            '--頻率',
            type=int,
            default=44100,
        )

    def 全部資料(self, *args, **參數):
        語料目錄 = join(settings.BASE_DIR, '語料', 'Suí-Siann')
        暫時檔案 = join(語料目錄, 'SuiSiann-0.1.tar')
        if not isfile(暫時檔案):
            makedirs(語料目錄, exist_ok=True)
            run(
                ['wget', '-O', 暫時檔案, self.網址],
                stdout=self.stdout, stderr=self.stderr, check=True
            )
        TarFile(暫時檔案).extractall(語料目錄)

        轉檔所在 = join(
            語料目錄, 'hue7jip8',
        )
        音檔目錄 = join(
            語料目錄, '0.1', 'ImTong',
        )
        轉檔目錄 = join(
            轉檔所在, 'ImTong',
        )
        makedirs(轉檔目錄, exist_ok=True)
        音檔陣列 = []
        for 檔名 in sorted(listdir(音檔目錄)):
            來源 = join(音檔目錄, 檔名)
            目標 = join(轉檔目錄, 檔名)
            print(來源)
            run([
                'ffmpeg', '-i',
                來源,
                '-acodec', 'pcm_s16le',
                '-ar', '{}'.format(參數['頻率']),
                '-ac', '1',
                '-y',
                目標,
            ], stdout=self.stdout, stderr=self.stderr, check=True)
            音檔陣列.append(目標)

        with open(
            join(語料目錄, '0.1', 'sui-siann.csv')
        ) as tong:
            for 一逝 in DictReader(tong):
                yield 訓練過渡格式(
                    影音所在=join(轉檔所在, 一逝['音檔']),
                    文本=拆文分析器.建立句物件(一逝['漢字'], 一逝['羅馬字']).看分詞(),
                    **self.公家內容
                )

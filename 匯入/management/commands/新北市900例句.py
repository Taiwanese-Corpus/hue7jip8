from os import makedirs
from os.path import join, isfile
from posix import listdir
from subprocess import run
from urllib.request import urlretrieve
from zipfile import ZipFile

from django.conf import settings


from 臺灣言語服務.models import 訓練過渡格式
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3'

    公家內容 = {
        '來源': '新北市104學年度閩南語字音字形-臺語上美麗辭典揣舉例-900例句工作坊',
        '影音語者': '王秀容',
        '種類': '語句',
        '年代': '2015',
    }
    網址 = 'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3/archive/master.zip'

    def add_arguments(self, parser):
        parser.add_argument(
            '--頻率',
            type=int,
            default=44100,
        )

    def 全部資料(self, *args, **參數):
        語料目錄 = join(settings.BASE_DIR, '語料', '新北市900例句')
        makedirs(語料目錄, exist_ok=True)
        暫時檔案 = join(語料目錄, 'master.zip')
        if not isfile(暫時檔案):
            urlretrieve(self.網址, 暫時檔案)
        ZipFile(暫時檔案).extractall(語料目錄)
        音檔目錄 = join(
            語料目錄, 'Sin1pak8tshi7_2015_900-le7ku3-master', '鉸好的1-150音檔'
        )
        轉檔目錄 = join(
            語料目錄, 'Sin1pak8tshi7_2015_900-le7ku3-master', '鉸好的1-150音檔-轉好'
        )
        makedirs(轉檔目錄, exist_ok=True)
        音檔陣列 = []
        for 檔名 in sorted(listdir(音檔目錄), key=lambda 名: int(名.split('.')[0])):
            來源 = join(音檔目錄, 檔名)
            目標 = join(轉檔目錄, 檔名)
            run([
                'ffmpeg', '-i',
                來源,
                '-acodec', 'pcm_s16le',
                '-ar', '{}'.format(參數['頻率']),
                '-ac', '1',
                '-y',
                目標,
            ], check=True)
            音檔陣列.append(目標)

        with open(
            join(語料目錄, 'Sin1pak8tshi7_2015_900-le7ku3-master', 'minnan900.分詞')
        ) as 分詞檔案:
            for 一逝分詞, 音檔路徑 in zip(分詞檔案.readlines(), 音檔陣列):
                yield 訓練過渡格式(
                    影音所在=音檔路徑,
                    文本=一逝分詞.strip(),
                    **self.公家內容
                )

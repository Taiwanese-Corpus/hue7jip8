from os import makedirs
from os.path import join
from posix import listdir

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from libavwrapper.avconv import Input, Output, AVConv
from libavwrapper.codec import AudioCodec, NO_VIDEO


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--匯入幾筆',
            type=int,
            default=100000,
            help='試驗用，免一擺全匯'
        )

    def handle(self, *args, **參數):
        語料目錄 = join(
            settings.BASE_DIR, '語料', '教育部閩南語常用詞辭典',
            'twblg.dict.edu.tw', 'holodict_new', 'audio',
        )
        目標目錄 = join(settings.BASE_DIR, '語料', '教育部閩南語常用詞辭典wav')
        makedirs(目標目錄, exist_ok=True)
        匯入數量 = 0
        for 檔名 in sorted(listdir(語料目錄)):
            if 檔名.endswith('.mp3'):
                來源 = join(語料目錄, 檔名)
                目標 = join(目標目錄, 檔名[:-4] + '.wav')
                目標聲音格式 = AudioCodec('pcm_s16le')
                目標聲音格式.channels(1)
                目標聲音格式.frequence(16000)
                原始檔案 = Input(來源)
                網頁檔案 = Output(目標).overwrite()
                指令 = AVConv('avconv', 原始檔案, 目標聲音格式, NO_VIDEO, 網頁檔案)
                程序 = 指令.run()
                程序.wait()

                匯入數量 += 1
                if 匯入數量 == 參數['匯入幾筆']:
                    break

        call_command('顯示資料數量')

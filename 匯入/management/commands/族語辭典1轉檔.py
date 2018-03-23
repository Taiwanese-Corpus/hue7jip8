from os import makedirs
from os.path import join
from posix import listdir

from django.conf import settings
from django.core.management.base import BaseCommand

from libavwrapper.avconv import Input, Output, AVConv
from libavwrapper.codec import AudioCodec, NO_VIDEO


from 匯入.族語辭典 import 代碼對應


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '語言',
            type=str,
            help='選擇的族語'
        )

    def handle(self, *args, **參數):
        # 檢查avconv有裝無
        代碼 = 代碼對應[參數['語言']]
        語料目錄 = join(settings.BASE_DIR, '語料', '族語辭典', 代碼)
        目標目錄 = join(settings.BASE_DIR, '語料', '族語辭典wav', 代碼)
        makedirs(目標目錄, exist_ok=True)
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

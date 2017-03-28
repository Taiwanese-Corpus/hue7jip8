import json
from os.path import join
from posix import listdir
from urllib.request import urlopen

from django.conf import settings
from django.core.management.base import BaseCommand

from libavwrapper.avconv import Input, Output, AVConv
from libavwrapper.codec import AudioCodec, NO_VIDEO


class Command(BaseCommand):

    def handle(self, *args, **參數):
        # 檢查avconv有裝無
        語料目錄 = join(settings.BASE_DIR, '族語辭典')
        for 檔名 in sorted(listdir(語料目錄)):
            if 檔名.endswith('.mp3'):
                來源 = join(語料目錄, 檔名)
                目標 = '.'.join(來源.split('.')[:-1]) + '.wav'
                目標聲音格式 = AudioCodec('pcm_s16le')
                目標聲音格式.channels(1)
                目標聲音格式.frequence(16000)
                原始檔案 = Input(來源)
                網頁檔案 = Output(目標).overwrite()
                指令 = AVConv('avconv', 原始檔案, 目標聲音格式, NO_VIDEO, 網頁檔案)
                程序 = 指令.run()
                程序.wait()

import json
from os.path import join
from urllib.request import urlopen

from django.core.management.base import BaseCommand
from libavwrapper.avconv import Input, Output, AVConv
from libavwrapper.codec import AudioCodec, NO_VIDEO


class Command(BaseCommand):

    def handle(self, *args, **參數):
        # 檢查avconv有裝無
        網頁聲音格式 = AudioCodec('libmp3lame')
        網頁聲音格式.channels(1)
        網頁聲音格式.frequence(16000)
        網頁聲音格式.bitrate('128k')
        原始檔案 = Input(self.影音所在())
        網頁檔案 = Output(所在)
        指令 = AVConv('avconv', 原始檔案, 網頁聲音格式, NO_VIDEO, 網頁檔案)
        程序 = 指令.run()
        結果 = 程序.wait()

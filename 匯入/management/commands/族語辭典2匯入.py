import json
from os.path import join, splitext, basename, isfile
from urllib.parse import urlparse
from urllib.request import urlopen

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語資料庫.資料模型 import 影音表
from 匯入.族語辭典 import 代碼對應


class Command(BaseCommand):
    help = 'https://github.com/thewayiam/ami_dict_crawler'

    def add_arguments(self, parser):
        parser.add_argument(
            '語言',
            type=str,
            help='選擇的族語'
        )

    def handle(self, *args, **參數):
        call_command('顯示資料數量')

        代碼 = 代碼對應[參數['語言']]
        with urlopen(
            # 'https://github.com/thewayiam/ami_dict_crawler/raw/master/data/data.json'
            'https://github.com/Taiwanese-Corpus/ami_dict_crawler/raw/master/data/{}.json'
            .format(代碼)
        ) as 資料檔案:
            資料 = json.loads(資料檔案.read().decode('utf-8'))
        全部資料 = []
        for 一筆 in 資料:
            錄音檔網址 = 一筆['pronounce']
            全部資料.append(('字詞', 一筆['name'], 錄音檔網址))
            for 例句 in 一筆['examples']:
                錄音檔網址 = 例句['pronounce']
                全部資料.append(('語句', 例句['sentence'], 錄音檔網址))

        公家內容 = {
            '收錄者': 來源表.objects.get_or_create(名='系統管理員')[0].編號(),
            '來源': 來源表.objects.get_or_create(名='原住民族語言線上詞典')[0].編號(),
            '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
            '語言腔口': 參數['語言'],
            '著作所在地': '臺灣',
            '著作年': str(2016),
            '屬性': {'語者': '族語辭典'}
        }
        匯入數量 = 0
        語料目錄 = join(settings.BASE_DIR, '語料', '族語辭典wav', 代碼)
        for (種類, 詞條, mp3網址音檔) in 全部資料:
            if mp3網址音檔 is not None:
                wav音檔 = join(
                    語料目錄,
                    splitext(basename(urlparse(mp3網址音檔).path))[0] + '.wav'
                )
                if 詞條 and isfile(wav音檔):
                    影音內容 = {'影音所在': wav音檔, '種類': 種類}
                    影音內容.update(公家內容)
                    影音 = 影音表.加資料(影音內容)
                    文本內容 = {'文本資料': 詞條, '種類': 種類}
                    文本內容.update(公家內容)
                    影音.寫文本(文本內容)

                    匯入數量 += 1
                    if 匯入數量 % 100 == 0:
                        print('匯入數量 {}'.format(匯入數量))
        call_command('顯示資料數量')

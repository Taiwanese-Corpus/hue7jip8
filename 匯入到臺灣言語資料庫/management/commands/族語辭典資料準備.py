import json
from os import makedirs
from os.path import join
from random import randint
from time import sleep
from urllib.parse import quote
from urllib.request import urlopen, urlretrieve

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'https://github.com/thewayiam/ami_dict_crawler'

    def handle(self, *args, **參數):
        語料目錄 = join(settings.BASE_DIR, '族語辭典')
        makedirs(語料目錄, exist_ok=True)
        with urlopen(
            # 'https://github.com/thewayiam/ami_dict_crawler/raw/master/data/data.json'
            'https://github.com/Taiwanese-Corpus/ami_dict_crawler/raw/master/data/data.json'
        ) as 資料檔案:
            資料 = json.loads(資料檔案.read().decode('utf-8'))
        全部錄音檔 = []
        for 一筆 in 資料:
            錄音檔網址 = 一筆['pronounce']
            if 錄音檔網址 is not None:
                全部錄音檔.append(錄音檔網址)
            for 例句 in 一筆['examples']:
                錄音檔網址 = 例句['pronounce']
                if 錄音檔網址 is not None:
                    全部錄音檔.append(錄音檔網址)
        if len(全部錄音檔) != len(set(全部錄音檔)):
            raise RuntimeError('有仝網址的音檔')
        錄音檔對應 = {}
        for 網址 in 全部錄音檔:
            sleep(randint(10, 20))
            所在 = join(語料目錄, 網址.split('/')[-1])
            urlretrieve(quote(網址, safe='/:'), 所在)
            錄音檔對應[網址] = 所在
        with open(join(語料目錄, '錄音檔對應.json'), 'w') as 檔案:
            json.dump(錄音檔對應, 檔案, sort_keys=True, indent=2)

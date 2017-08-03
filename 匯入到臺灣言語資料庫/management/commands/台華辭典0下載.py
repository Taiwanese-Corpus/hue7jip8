from os.path import join
from django.core.management.base import BaseCommand
import json
from django.conf import settings
from pkg_resources.py31compat import makedirs
import csv
from urllib.request import urlopen


class Command(BaseCommand):

    def handle(self, *args, **參數):
        語料目錄 = join(settings.BASE_DIR, '語料', '台華辭典')
        makedirs(語料目錄, exist_ok=True)
        with urlopen(
            'https://raw.githubusercontent.com/Taiwanese-Corpus/Tinn-liong-ui_2000_taihoa-dictionary/master/%E6%95%99%E8%82%B2%E9%83%A8%E5%BB%BA%E8%AD%B0%E7%94%A8%E5%AD%97/Taihoa.csv'
        ) as 資料檔案:
            全部資料 = 資料檔案.read().decode('utf-8')
            資料 = json.loads(全部資料)
            
            輸出檔 = csv.DictWriter(
                '台華辭典.csv', fieldnames=['ID',
                    '台語羅馬字',
                    '台語羅馬字2',
                    '台語漢字',
                    '華語對譯',
                    '英文',
                    'freq',
                    'pos_h',
                ]
            )
            輸出檔.writeheader()
            
            for 一逝 in 資料:
                輸出檔.writerow([一逝['ID'],
                    一逝['台語羅馬字'],
                    一逝['台語羅馬字2'],
                    一逝['台語漢字'],
                    一逝['華語對譯'],
                    一逝['英文'],
                    一逝['freq'],
                    一逝['pos_h']]
                )
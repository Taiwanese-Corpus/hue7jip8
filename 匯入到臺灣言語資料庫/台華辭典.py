from os.path import join
from django.conf import settings
from os import makedirs
from urllib.request import urlopen
import json
import csv
import io
from csv import DictReader

def 下載():
    語料目錄 = join(settings.BASE_DIR, '語料', '台華辭典')
    makedirs(語料目錄, exist_ok=True)
    with urlopen(
        'https://raw.githubusercontent.com/Taiwanese-Corpus/Tinn-liong-ui_2000_taihoa-dictionary/master/%E6%95%99%E8%82%B2%E9%83%A8%E5%BB%BA%E8%AD%B0%E7%94%A8%E5%AD%97/Taihoa.csv'
    ) as 資料檔案:
        全部資料csv = 資料檔案.read().decode('utf-8')
        with io.StringIO(全部資料csv) as 詞目:
            讀檔 = DictReader(詞目)
            輸出陣列 = []
            for 一逝 in 讀檔:
                輸出陣列.append(一逝)
            return 輸出陣列
    
def 匯入():
    return

def 匯入一筆():
    return
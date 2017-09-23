import json
from os.path import join

from django.core.management.base import BaseCommand


from 臺灣言語資料庫.資料模型 import 影音表
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語資料庫.資料模型 import 資料表工具


class Command(BaseCommand):
    help = '匯入高明達聽拍的資料庫'

    def add_arguments(self, parser):
        parser.add_argument(
            '聽拍json',  type=str
        )
        parser.add_argument(
            'wav資料夾所在',  type=str
        )

    def handle(self, *args, **參數):
        self.stdout.write(資料表工具.顯示資料數量())
        公家內容 = {
            '收錄者': 來源表.objects.get_or_create(名='系統管理員')[0],
            '來源': {'名': '台文資料庫'},
            '版權': 版權表.objects.get_or_create(版權='會使公開')[0],
            '種類': '語句',
            '語言腔口': '臺語',
            '著作所在地': '臺灣',
            '著作年': '2017',
        }
        with open(參數['聽拍json']) as 檔案:
            for 資料 in json.load(檔案):
                影音內容 = {'影音所在': join(參數['wav資料夾所在'], 資料['影音所在'])}
                影音內容.update(公家內容)
                影音 = 影音表.加資料(影音內容)
                聽拍內容 = {'聽拍資料': 資料['聽拍資料']}
                聽拍內容.update(公家內容)
                影音.寫聽拍(聽拍內容)
        self.stdout.write(資料表工具.顯示資料數量())

from django.core.management.base import BaseCommand
from 匯入到臺灣言語資料庫.台華辭典 import 下載
from 匯入到臺灣言語資料庫.台華辭典 import 匯入


class Command(BaseCommand):

    def handle(self, *args, **參數):
        台華辭典陣列 = 下載()
        匯入(台華辭典陣列)

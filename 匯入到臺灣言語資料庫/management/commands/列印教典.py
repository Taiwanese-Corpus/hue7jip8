from django.core.management.base import BaseCommand
from 匯入到臺灣言語資料庫.台華辭典 import 下載
from 匯入到臺灣言語資料庫.台華辭典 import 匯入
from django.core.management import call_command
from 匯入到臺灣言語資料庫.台華辭典 import 列印辭典
from 匯入到臺灣言語資料庫.教育部閩南語常用詞辭典.教典 import 教典


class Command(BaseCommand):

    def handle(self, *args, **參數):
        一教典物件 = 教典()
        一教典物件.列印辭典()
        
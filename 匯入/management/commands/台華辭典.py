from django.core.management.base import BaseCommand
from 匯入.台華辭典 import 下載
from 匯入.台華辭典 import 匯入
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **參數):
        # 呼叫語言資料庫的內建函式，顯示目前各個表格的數量
        call_command('顯示資料數量')
        # 下載並匯入台華辭典到語言資料庫
        台華辭典陣列 = 下載()
        匯入(台華辭典陣列)
        # 呼叫語言資料庫的內建函式，確認外語表和文本表的數量有改變
        call_command('顯示資料數量')

from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式


class Command(BaseCommand):

    def handle(self, *args, **參數):
        self.stdout.write('資料數量：{}'.format(訓練過渡格式.資料數量()))
        with open('han.txt', 'w') as han:
            with open('lo.txt', 'w') as lo:
                with open('hua.txt', 'w') as hua:
                    for mih in 訓練過渡格式.objects.all():
                        句物件 = 拆文分析器.分詞句物件(mih.文本)
                        print(句物件.看語句(), file=han)
                        print(句物件.看音(), file=lo)
                        print(拆文分析器.分詞句物件(mih.外文).看語句(), file=hua)

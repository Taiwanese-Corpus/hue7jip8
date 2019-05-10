from http.client import HTTPSConnection
import json
from urllib.parse import quote


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 匯入.指令 import 匯入枋模


class Command(匯入枋模):
    help = 'https://itaigi.tw'
    domain = 'itaigi.tw'
    網址 = '/匯出資料'

    公家內容 = {
        '來源': 'itaigi',
        '種類': '字詞',
        '年代': '2018',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 一條 in self._全部資料():
            if 一條['來源'] in ['臺灣閩南語常用詞辭典', '台文華文線頂辭典']:
                continue
            for 羅馬字 in 一條['羅馬字'].split('/'):
                try:
                    台語物件 = 拆文分析器.建立句物件(一條['漢字'], 羅馬字)
                except 解析錯誤:
                    print('「{}」「{}」無對齊!'.format(一條['漢字'], 一條['羅馬字']))
                    continue
                try:
                    外文物件 = 拆文分析器.建立句物件(一條['華語'])
                except 解析錯誤 as 錯誤:
                    print(錯誤)
                    continue
                yield 訓練過渡格式(
                    文本=台語物件.看分詞(),
                    外文=外文物件.看分詞(),
                    **self.公家內容
                )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 條'.format(匯入數量))

    def _全部資料(self):
        conn = HTTPSConnection(self.domain)
        conn.request("GET", quote(self.網址))
        r1 = conn.getresponse()
        if r1.status != 200:
            raise RuntimeError('連線錯誤：{}{}\n{} {}'.format(
                self.domain, self.網址, r1.status, r1.reason
            ))
        內容 = r1.read().decode()
        return json.loads(內容)['資料']

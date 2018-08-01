from http.client import HTTPSConnection
import json
import ssl
from urllib.parse import quote


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 匯入.指令 import 匯入枋模


ssl.match_hostname = lambda cert, hostname: True


class Command(匯入枋模):
    help = 'https://詞彙分級.意傳.台灣'
    domain = 'xn--kbr112a4oa73rtw5adwqr1d.xn--v0qr21b.xn--kpry57d'
    網址 = '/匯出資料庫'

    公家內容 = {
        '來源': '詞彙分級',
        '種類': '語句',
    }

    def 全部資料(self, *args, **參數):
        匯入數量 = 0
        for 一篇 in self._全部資料():
            年代 = '2018'
            for 一逝 in 一篇['文章資料']:
                try:
                    台語物件 = 拆文分析器.建立句物件(一逝['漢字'], 一逝['臺羅'])
                except 解析錯誤:
                    print('第 {} 篇 漢羅有無對齊的!'.format(一篇['id']))
                except 型態錯誤:
                    print('第 {} 篇 漢羅無平長!'.format(一篇['id']))
                else:
                    yield 訓練過渡格式(
                        文本=台語物件.看分詞(),
                        年代=年代,
                        **self.公家內容
                    )

            匯入數量 += 1
            if 匯入數量 % 1000 == 0:
                self.stdout.write('匯入 {} 篇'.format(匯入數量))

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

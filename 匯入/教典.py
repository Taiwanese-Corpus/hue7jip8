from 臺灣言語工具.基本物件.公用變數 import 標點符號


def 字詞抑是語句(漢, 羅):
    if 漢[-1] in 標點符號 and 漢[-1] in 標點符號:
        return '語句'
    return '字詞'

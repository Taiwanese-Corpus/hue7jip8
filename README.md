# Huē-ji̍p
[![PyPI version](https://badge.fury.io/py/hue7jip8.svg)](https://badge.fury.io/py/hue7jip8)
[![Build Status](https://travis-ci.org/Taiwanese-Corpus/hue7jip8.svg?branch=master)](https://travis-ci.org/Taiwanese-Corpus/hue7jip8)
[![Coverage Status](https://coveralls.io/repos/github/Taiwanese-Corpus/hue7jip8/badge.svg?branch=master)](https://coveralls.io/github/Taiwanese-Corpus/hue7jip8?branch=master)

匯入語料專案，目前語料都放在[Taiwanese-Corpus Github](https://github.com/Taiwanese-Corpus)，各專案詳細內容請洽各專案README。

會當參考服務的[文件](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_hok8-bu7/wiki/%E5%BF%AB%E9%80%9F%E8%AA%AA%E6%98%8E#%E8%A8%93%E7%B7%B4%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90%E6%A8%A1%E5%9E%8B)

## 台語

### [臺灣閩南語常用詞辭典-詞條](http://twblg.dict.edu.tw/holodict_new/index.htm)
- 形式：全漢、全羅
- 句數：28830（2018/07/18）
- 語料：[Github](https://github.com/g0v/moedict-data-twblg/tree/master/uni)
```
python manage.py 教典詞條
```

### [臺灣閩南語常用詞辭典-例句](http://twblg.dict.edu.tw/holodict_new/index.htm)
- 形式：全漢、全羅
- 句數：13835（2018/07/05）
- 語料：[Github](https://github.com/g0v/moedict-data-twblg/tree/master/uni)
```
python manage.py 教典例句
```

### [TGB通訊](http://taioanchouhap.pixnet.net/blog)
- 形式：漢羅、華語平行語料
- 句數：35017（2018/07/05）
- 語料：[Github](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3#%E6%8F%90%E8%91%97tgb%E5%B9%B3%E8%A1%8C%E8%AA%9E%E6%96%99)
```
python manage.py TGB通訊
```

### [iCorpus台華平行新聞語料庫](http://icorpus.iis.sinica.edu.tw/)
- 形式：全羅、華語平行語料
- 句數：83544（2018/07/05）
- 語料：[Github](https://github.com/sih4sing5hong5/icorpus)
```bash
python manage.py icorpus臺華平行新聞語料庫
```

### [教育部詞彙分級計劃](https://詞彙分級.意傳.台灣/)
- 形式：全漢、全羅
- 句數：61354句（2018/07/05）
- 語料：[API](https://詞彙分級資料庫.意傳.台灣/匯出資料庫)
```
python manage.py 詞彙分級
```

### [台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計](http://ip194097.ntcu.edu.tw/giankiu/keoe/KKH/guliau-supin/guliau-supin.asp)
- 形式：漢羅抑是全羅
- 段數：193071段， 其中漢羅128505段、全羅64566段（2018/07/24）
- 語料：[Github](https://github.com/Taiwanese-Corpus/Ungian_2005_guliau-supin)
```
python manage.py 台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計
``` 

### [台語文數位典藏資料庫](https://github.com/Taiwanese-Corpus/nmtl_2006_dadwt)
- 形式：漢羅、全羅
- 段數：67005段，其中62246段對會齊，4759段無法度對齊就用羅馬字（2018/07/30）
- 語料：[Github](https://github.com/Taiwanese-Corpus/nmtl_2006_dadwt)
```
python manage.py 台語文數位典藏資料庫
``` 

### [教育部臺灣閩南語字詞頻調查工作](http://ip194097.ntcu.edu.tw/Ungian/Chokphin/Lunbun/KIPsupin/KIPsupin.asp)
- 形式：漢羅、全羅
- 段數：59300段，其中53593段對會齊，5707段無法度對齊就用羅馬字（2018/07/24）
- 語料：[Github](https://github.com/Taiwanese-Corpus/Ungian_2009_KIPsupin)
```
python manage.py 教育部臺灣閩南語字詞頻調查工作
```  

### [白話字文獻館](http://pojbh.lib.ntnu.edu.tw)
- 形式：漢羅、全羅
- 段數：43493段，其中31195段對會齊，12298段無法度對齊就用羅馬字（2018/07/31）
- 語料：[Github](https://github.com/Taiwanese-Corpus/Khin-hoan_2010_pojbh)
```
python manage.py 白話字文獻館
``` 

### [台灣植物名彙](http://ip194097.ntcu.edu.tw/memory/TGB/thak.asp?id=59&page=4)
- 形式：羅馬字、華語漢字
- 句數：354詞（2018/07/24）
- 語料：[Github](https://github.com/Taiwanese-Corpus/Syuniti-Sasaki_1928_List-of-Plants-of-Formosa)
```
python manage.py 台灣植物名彙
```


### [台灣白話基礎語句](http://ip194097.ntcu.edu.tw/memory/TGB/thak.asp?id=862)
- 形式：羅馬字、華語漢字
- 句數：61354詞翻譯對照（2018/07/24）
- 語料：[Github](https://github.com/Taiwanese-Corpus/Ko-Chek-hoan-Tan-Pang-tin_1956_Basic-Vocabulary-for-Colloquial-Taiwanese)
```
python manage.py 台灣白話基礎語句
```


### 服務文件
## 族語
### [族語辭典](https://github.com/thewayiam/ami_dict_crawler)
```
python manage.py 族語辭典0下載 Pangcah # 完整匯入。較慢，愛五六工
# python manage.py 族語辭典0下載 Pangcah --下載幾筆 10 # 匯入10筆就好，試驗用
python manage.py 族語辭典1轉檔 Pangcah
python manage.py 族語辭典2匯入 Pangcah
```
語言代碼請[參考程式](https://github.com/sih4sing5hong5/hue7jip8/blob/master/%E5%8C%AF%E5%85%A5%E5%88%B0%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB/%E6%97%8F%E8%AA%9E%E8%BE%AD%E5%85%B8.py#L1)。下載好的[音檔](https://www.dropbox.com/s/68ot9f8lhjoa9pb/%E6%97%8F%E8%AA%9E%E8%BE%AD%E5%85%B8.tar?dl=0)在這。

## 台語
### 教典詞條音檔
- 形式：全漢、全羅
- 詞數：
- 語者：王秀容
```
python manage.py 教典音檔0下載 dropbox # 20160926掠的版本
# python manage.py 教典音檔0下載 官網沓沓掠 # 較慢，愛一工
python manage.py 教典音檔1轉檔 # 轉全部mp3音檔做16000Hz的wav
# python manage.py 教典音檔1轉檔 --匯入幾筆 100 # 轉100筆就好，試驗用
python manage.py 教典音檔2匯入 # 完整匯入
# python manage.py 教典音檔2匯入 --匯入幾筆 100 # 匯入100筆就好，試驗用
```

### [新北市900例句](https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3)
- 形式：全漢、全羅
- 句數：150句
- 語者：王秀容
```
python manage.py 新北市900例句 --頻率 16000 # 原始音檔頻率44100Hz
```
準做欲用秀容老師的聲，請配合教典做伙用，無訓練會[產生錯誤](https://github.com/sih4sing5hong5/hue7jip8/pull/7#issuecomment-298552263)


### [台文/華文線頂辭典](https://github.com/Taiwanese-Corpus/Tinn-liong-ui_2000_taihoa-dictionary)
形式：台華英辭典
詞數：
```
python manage.py 台華辭典
```

### [臺灣閩南語卡拉OK正字字表](https://github.com/Taiwanese-Corpus/moe_minkalaok)
  * pdf→純文字→臺灣言語資料庫yaml
  * 臺語→臺語
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/moe_minkalaok/閩南語卡拉OK正字字表.yaml
```

### [iCorpus台華平行新聞語料庫漢字臺羅版](https://github.com/Taiwanese-Corpus/icorpus_ka1_han3-ji7) 
  * 純文字→臺灣言語資料庫yaml
  * 白話字→全漢全羅
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/icorpus_ka1_han3-ji7/臺華平行新聞語料庫.yaml
```

### [咱的字你敢捌－台語漢字](https://github.com/Taiwanese-Corpus/Linya-Huang_2014_taiwanesecharacters)
  * html→臺灣言語資料庫yaml
  * 臺語→臺語
  * 988筆文本資料
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/Linya-Huang_2014_taiwanesecharacters/咱的字你敢捌.yaml
```


### [臺語國校仔課本](https://github.com/Taiwanese-Corpus/kok4hau7-kho3pun2)
  * 允言整理過的doc→json→臺灣言語資料庫yaml
  * 全漢全羅
  0* `https://taiwanese-corpus.github.io/kok4hau7-kho3pun2/臺語國校仔課本.yaml`

### [新約聖經語料](https://github.com/Taiwanese-Corpus/Pakhelke-1916_KoTan-1975_hiantaiekpun-2008_taiwanese-bible)
  * 允言整理過的doc→json→臺灣言語資料庫yaml
  * 全漢全羅
  * `https://Taiwanese-Corpus.github.io/Pakhelke-1916_KoTan-1975_hiantaiekpun-2008_taiwanese-bible/新約聖經語料.yaml`

### 猶未整理
遮的語料攏猶未提供臺灣言語資料庫yaml格式，毋過大部份攏好處理。語料專案照處理方法排：%8F%E8%B3%87%E6%96%99%E5%BA%AB.yaml`
* [荷華文語類參](https://github.com/Taiwanese-Corpus/Schlegel-Gustave_1886_Nederlandsch-Chineesch-Woordenboek)
  * xls
* [厦荷詞典](https://github.com/Taiwanese-Corpus/J.-J.-C.-Francken_C.-F.-M.-de-Grijs_1882_Chineesch-Hollandsch_woordenboek-van-het-Emoi-dialekt)
  * xls
* [駱嘉鵬老師華語臺語客語文件-字典、對應表](https://github.com/Taiwanese-Corpus/Loh_2004_hanyu-document)
  * xls
* [Embree台英辭典](https://github.com/Taiwanese-Corpus/Bernard-L.M.-Embree_1973_A-Dictionary-of-Southern-Min)
  * xls
* [廈英大辭典](https://github.com/Taiwanese-Corpus/Carstairs-Douglas_1873_chinese-english-dictionary)
  * doc→csv
* [台日大辭典台語譯本](https://github.com/Taiwanese-Corpus/Ogawa-Naoyoshi_1931-1932)
  * sql→csv
* [吳守禮《國臺對照活用辭典》電子化](https://github.com/Taiwanese-Corpus/koktai)
  * 專案內，有parser會當轉做jade格式
* [華台語文對譯](https://github.com/Taiwanese-Corpus/Ungian_hoatai-courses)
  * html+xls+pdf
  * （華語→）臺語
* [猶未整理的語料](https://github.com/Taiwanese-Corpus/unclassified_corpus)
  * csv、xls…
* [網路語料](https://github.com/Taiwanese-Corpus/internet_corpus)

## 客家話
### [教育部臺灣客家語常用詞辭典](https://github.com/Taiwanese-Corpus/moedict-data-hakka/tree/%E8%BD%89%E5%88%B0%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB/%E8%BD%89%E5%88%B0%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB)
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/moedict-data-hakka/臺灣客家語常用詞辭典網路版語料.yaml
```

### [客語能力認證資料檔](https://github.com/Taiwanese-Corpus/hakka_elearning)
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/hakka_elearning/臺灣客話詞彙資料庫語料.yaml
```

### 猶未整理
* [天光客語辭典](https://github.com/Taiwanese-Corpus/moedict-data-tiengong)

## 族語
### [族語E樂園](https://github.com/Taiwanese-Corpus/moedict-data-twblg/tree/gh-pages/%E8%BD%89%E5%88%B0%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB)
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/klokah_data_extract/族語E樂園.yaml
```

### [阿美語方敏英字典Virginia Fey's Amis Dictionary](https://github.com/Taiwanese-Corpus/amis-data)
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/amis-data/dict-amis.yaml
```

### 猶未整理
* [原住民族語言線上詞典](http://e-dictionary.apc.gov.tw/Index.htm)
* [Dictionnaire Amis-Français](https://github.com/Taiwanese-Corpus/amis-francais)
* [蔡中涵委員阿美語字典](https://github.com/Taiwanese-Corpus/amis-safolu)
* [噶哈巫語分類辭典](https://github.com/Taiwanese-Corpus/kaxabu-muwalak-misa-a-ahan-bizu)

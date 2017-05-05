# 匯入到臺灣言語資料庫
[![Build Status](https://travis-ci.org/sih4sing5hong5/hue7jip8.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/hue7jip8)
[![Coverage Status](https://coveralls.io/repos/github/sih4sing5hong5/hue7jip8/badge.svg?branch=master)](https://coveralls.io/github/sih4sing5hong5/hue7jip8?branch=master)

會當參考服務的[文件](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_hok8-bu7/wiki/%E5%BF%AB%E9%80%9F%E8%AA%AA%E6%98%8E#%E8%A8%93%E7%B7%B4%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90%E6%A8%A1%E5%9E%8B)

## 族語
### [族語辭典](https://github.com/thewayiam/ami_dict_crawler)
```
python manage.py 族語辭典0下載 Pangcah --下載幾筆 10 # 匯入10筆就好，試驗用
python manage.py 族語辭典0下載 Pangcah # 完整匯入。較慢，愛五六工
python manage.py 族語辭典1轉檔 Pangcah
python manage.py 族語辭典2匯入 Pangcah
python manage.py 訓練HTS Pangcah 族語辭典
```
語言代碼請[參考程式](https://github.com/sih4sing5hong5/hue7jip8/blob/master/%E5%8C%AF%E5%85%A5%E5%88%B0%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB/%E6%97%8F%E8%AA%9E%E8%BE%AD%E5%85%B8.py#L1)

## 閩南語
```
python manage.py 教典音檔0下載 dropbox # 20160926掠的版本
python manage.py 教典音檔0下載 官網沓沓掠 # 較慢，愛一工
python manage.py 教典音檔1轉檔 --匯入幾筆 100 # 轉100筆就好，試驗用
python manage.py 教典音檔1轉檔 # 轉全部音檔
python manage.py 教典音檔2匯入 --匯入幾筆 100 # 匯入100筆就好，試驗用
python manage.py 教典音檔2匯入 # 完整匯入
python manage.py 訓練HTS 臺語 王秀容
```

### [新北市900例句](https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3)
```
python manage.py 新北市900例句 --頻率 16000 # 原始音檔頻率44100Hz
python manage.py 訓練HTS 臺語 王秀容
```
準做欲用秀容老師的聲，請配合教典做伙用，無訓練會[產生錯誤](https://github.com/sih4sing5hong5/hue7jip8/pull/7#issuecomment-298552263)

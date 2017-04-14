#!/bin/bash
prog="wget"
#prog="echo"
log_path="log"

cd 匯入到臺灣言語資料庫/教育部閩南語常用詞辭典

for i in $(seq -w 1 62000)
do
	url="http://twblg.dict.edu.tw/holodict_new/audio/$i.mp3"
	$prog -r $url 2>> $log_path
	echo $url
	declare -i sec=$RANDOM%2+1
	sleep $sec;
done


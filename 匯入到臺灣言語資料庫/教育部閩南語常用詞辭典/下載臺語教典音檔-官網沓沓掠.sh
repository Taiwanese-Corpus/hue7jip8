#!/bin/bash
prog="wget"
#prog="echo"
log_path="log"

DIR=$1
cd ${DIR}

for i in $(seq -w 1 62000)
do
	url="http://twblg.dict.edu.tw/holodict_new/audio/$i.mp3"
	$prog -r $url 2>> $log_path
	echo $url
	declare -i sec=$RANDOM%2+1
	sleep $sec;
done


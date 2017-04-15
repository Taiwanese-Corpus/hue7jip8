#!/bin/bash
function decoding(){
  mp3_filename=`basename $1`
  wav_filename="${mp3_filename%.*}".wav
  avconv -loglevel error -y -i "$1" -vcodec copy -ac 1 -strict experimental 匯入到臺灣言語資料庫/教育部閩南語常用詞辭典/wav/"$wav_filename";
}
mkdir -p 匯入到臺灣言語資料庫/教育部閩南語常用詞辭典/wav
export -f decoding
echo 匯入到臺灣言語資料庫/教育部閩南語常用詞辭典/twblg.dict.edu.tw/holodict_new/audio/*.mp3 |\
  xargs -n 1 -P 4 bash -c 'decoding "$@"' _ 

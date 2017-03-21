#!/bin/bash
function decoding(){
  mp3_filename=`basename $1`
  wav_filename="${mp3_filename%.*}".wav
  avconv -y -i "$1" -vcodec copy -ac 1 -ar 16000 -strict experimental 族語辭典/"$wav_filename";
}
export -f decoding
ls 族語辭典/*.mp3 |\
  xargs -n 1 -P 4 bash -c 'decoding "$@"' _ 

#/bin/bash
DIR=匯入到臺灣言語資料庫/教育部閩南語常用詞辭典
wget --directory-prefix=${DIR} https://www.dropbox.com/s/peh3gefzxvores1/twblg_audio_20160926.tar?dl=0
tar -xf ${DIR}/twblg_audio_20160926.tar?dl=0 -C ${DIR}

FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7
MAINTAINER i3thuan5

ARG TOX_ENV

RUN apt-get update && apt-get install -y ffmpeg
WORKDIR /opt/hue7jip8
RUN pip install tox
COPY . .
RUN tox --sitepackages -e ${TOX_ENV}

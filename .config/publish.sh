#!/bin/bash

DATA_SOURCE=/home/rkost/speedtests
FTP=vis.png
FTP_RAW=iperfRawData.zip
TARGET_FILE=/volume1/DATA_1/WebHosts/3_rkost-org/vodafone/2020-07/bandwidth-vis.png
TARGET_FILE_RAW=/volume1/DATA_1/WebHosts/3_rkost-org/vodafone/2020-07/iperfRawData.zip
TARGET_USER=rkost-local
TARGET_IP=10.10.0.10


cd /home/rkost/repos/iperf3Vis
source .venv/bin/activate

python src/run.py --data-directory ${DATA_SOURCE} --output ${FTP} --time-interval 1h

rsync -e "ssh -p 5101" -a ${FTP} ${TARGET_USER}@${TARGET_IP}:${TARGET_FILE}

# Accumulate raw data and publish
zip -9 -y -r -q ${FTP_RAW} ${DATA_SOURCE}
rsync -e "ssh -p 5101" -a ${FTP_RAW} ${TARGET_USER}@${TARGET_IP}:${TARGET_FILE_RAW}


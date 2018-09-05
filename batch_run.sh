#!/bin/bash
#
# Author : huanghailong9
#
# mail: huanghailong@jd.com
#
# Time : Thu 12 Apr 2018 20:18:49
#
#
set -x
start_day_str=$1
end_day_str=$2
#day_2_ago8_str=$3
start_day=$(date -d "$start_day_str" +%Y%m%d)
end_day=$(date -d "$end_day_str" +%Y%m%d)
#day_2_ago8=$(date -d "$day_2_ago8_str" +%Y%m%d)

while [ $end_day -lt $start_day ]
do
  hive -d day_1_ago8=$start_day  -f run.sql 
  echo $start_day
  start_day=$(date -d "$start_day 1 days ago" +%Y%m%d)
done

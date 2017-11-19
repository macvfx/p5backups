#!/bin/bash

# 1. check if P5 is running, if yes, then exit
# 2. if it is not running check for running python backup
# 3. if backup not running restart P5

if [ps aux |grep "ns[d] -u root" -eq 0]
then 
#check for python backups

else
# start p5 
/usr/local/aw/start-server
fi
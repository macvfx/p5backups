#!/bin/bash

# 1. check if P5 is running, if yes, then exit
# 2. if it is not running check for running python backup
# 3. if backup not running restart P5
stat=("pgrep -u root nsd")
if [[ $stat != 0 ]]; then
#start server
/usr/local/aw/start-server
echo "P5 now running"
else
echo "P5 already running"
fi
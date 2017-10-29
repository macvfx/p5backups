#!/usr/bin/env /usr/bin/python

import sys
import os
import commands
import subprocess
import sys
import shutil
import time

#
# where does your archiware install live (no trailing slash)
aw_path = "/usr/local/aw"
# where do you want to backup index and log files to?
backup_path = "/Volumes/Backups/aw-nightly-bkup/"

# check to see if nsd is already running, if it is lets throw a flag
nr = 0 # our flag
if(commands.getoutput('pgrep nsd') == ""):
	print "P5 is not running"
	nr = 1

# if P5 is running, lets check and make sure no jobs are running
if(nr != 1):
	# get all the running jobs
	jobs_str = subprocess.check_output([aw_path + "/bin/nsdchat","-c","Job","names"])
	jobs_str.rstrip()
	jobs = jobs_str.split()

	# figure out which are running and which are stopped.  We only care about running jobs
	i = 0
	for job in jobs:
		status = subprocess.check_output([aw_path + "/bin/nsdchat","-c","Job",job,"status"]).rstrip()
		if status == "running":
			i = i +1
			
	# if there is a running job, don't stop the service
	if i > 0:
		print "There are " + str(i) + " job(s) running, can't shut down service!"
		#exit()
		sys.exit(1)
	#if we can shut down P5, lets do it
	print "Shutting down P5"
	output = subprocess.check_output([aw_path + "/stop-server"])
	print output

# Lets make a backup of the files now, first we make a stamp so we know how long it took
time_start = time.time()

# Next we check to see if there is already a valid previous backup.  If there is, move it to keep it safe
print "Checking if there is existing backup"
if(os.path.isdir(backup_path + "/aw")):
	print "Existing backup found, moving old backup"
	if(os.path.isdir(backup_path + "/aw-old")):
		shutil.rmtree(backup_path + "/aw-old")
	shutil.move(backup_path + "/aw",backup_path + "/aw-old")
	
# After we make sure we can make a new copy, we copy the proper files	
print "Making backup copy"		
shutil.copytree(aw_path + "/config/index",backup_path + "/aw/config/index",symlinks=True)
shutil.copytree(aw_path + "/config/customerconfig",backup_path + "/aw/config/customerconfig",symlinks=True)
shutil.copytree(aw_path + "/log",backup_path + "/aw/log",symlinks=True)	
time_stop = time.time()

# Then we let you know how long it took
print "Backup took " + str(time_stop - time_start) + " seconds"

# Last, we start up the server
output = subprocess.check_output([aw_path + "/start-server"])
print output
sys.exit(0)
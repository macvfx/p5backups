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

# check to see if nsd is already running, if it is lets throw a flag
nr = 0 # our flag
if(commands.getoutput('pgrep nsd') == ""):
	print "P5 is not running"
	nr = 1

# if P5 is NOT running, let's restart it
if(nr != 0):
	
# Last, we start up the server
	output = subprocess.check_output([aw_path + "/start-server"])
	print output
	sys.exit(0)
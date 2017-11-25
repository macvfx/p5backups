#!/usr/bin/env /usr/bin/python

import sys
import os
import commands
import subprocess
import sys
import shutil
import time

print "p5 up"
# where does your archiware install live (no trailing slash)
aw_path = "/usr/local/aw"

# check to see if nsd is already running, if it is lets throw a flag
nr = 0 # our flag
print "commands.getoutput('pgrep nsd'):", commands.getoutput('pgrep nsdfoo')
if(commands.getoutput('pgrep nsd') == ""):
	print "P5 is not running"
	nr = 1

# if P5 is NOT running, let's restart it
if nr != 0:
	output = subprocess.check_output([aw_path + "/start-server"])
	print output
	sys.exit(0)
#!/bin/sh

#set your backup volume and folder to store the Archiware P5 backups
backupdir="/Users/Shared/Backup/AW/"
awconfig="/usr/local/aw/config/"
logfile="$backupdir/backup.log"
timeinfo=`date '+%F %T'`
echo "$timeinfo -> Starting P5 backup." >> $logfile
datestring=`date +%F_%H%M`

# copy P5 local files and database to Drive, NAS or anywhere
cp -Rf "/usr/local/aw/" "$backupdir/$datestring"
timeinfo=`date '+%F %T'`
echo "$timeinfo -> Finished P5 backup." >> $logfile

# this part is an example of copying data over to a NAS via ssh
#source1="/Volumes/Backup/More/Stuff/"
#source2="/Volumes/Backup/AWindex/"
#source3="/Volumes/Xsan1/NAS/Media"

# Rsync to NAS
#rsync -av "${source2}" -e ssh admin@10.2.1.1:/share/P5config >> $logfile
#rsync -av "${source3}" -e ssh admin@10.2.1.1:/share/Media >> $logfile

# Make a DMG of the Archiware P5 db 
hdiutil create -srcfolder "/usr/local/aw/" /Users/Shared/Backup/AW/p5_`date +%F`.dmg
#hdiutil create -srcfolder "${source2}" /Volumes/Backup/AW/p5archiveindex_$timeinfo.dmg

echo "$timeinfo -> Finished syncing." >> $logfile

#!/bin/bash

# Check if we are root privilage or not
if [[ ${UID} -ne 0 ]]
then
    echo "Please run this script with sudo or root"
    exit 1
fi


# Which files are we going to back up. Please make sure to exist /home/ec2-user/data file
backup_files="/home/ec2-user/data /home/ec2-user/myfolder" #/etc /boot /usr


# Where do we backup to. Please crete this file before execute this script
dest="/mnt/backup"


# Create archive filename based on time
time=$(date +"%Y_%m_%d_%H_%M")
hostname=$(hostname -s)
archive_file="${hostname}-${time}.tgz"


# Print start status message.
echo "Archive process is started"
date
echo

# Backup the files using tar.
#sudo tar -cvzf /mnt/backup/sample.tgz /home/ec2-user/data
sudo tar -cvzf ${dest}/${archive_file} ${backup_files}

# Print end status message.
echo 
echo "Congrulations! Your Backup is ready"


# Long listing of files in $dest to check file sizes.
ls -lh ${dest}


-------------

# To set this script for executing in every 5 minutes, we'll create cronjob

#!/bin/zsh
dt=`date '+%d/%m/%Y_%H:%M:%S'`
DOW=$(date '+%u')
while :
do
clear
echo "Started at $dt"
echo "Exiting script if today is a weekend..."
if [[ $DOW = 6 ]] # Saturday
    then exit
fi
if [[ $DOW = 7 ]] # Sunday
    then exit
fi
echo "."
dt=`date '+%d/%m/%Y_%H:%M:%S'`
echo "Starting script..."
/bin/python "/home/joey/coalemus/Python-Projects/selenium/meetgui.py"
echo "Ending script..."
echo "Completed at $dt"
echo "waiting for 40 minutes..."
sleep 40m
done
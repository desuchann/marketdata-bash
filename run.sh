#!/bin/bash

source config.sh

echo $(date)" **** Market monitor started **** " >> $LOGFILE

if wget -O data/raw/alphavprices_$DATE.csv --append-output="$LOGFILE" $URL1; then
    echo $(date)" **** Using primary API key **** " >> $LOGFILE

elif wget -O data/raw/alphavprices_$DATE.csv --append-output="$LOGFILE" $URL2; then
    echo $(date)" **** Using backup key **** " >> $LOGFILE
    
else
    echo $(date)" **** Both primary and backup API key urls failed **** "
    exit 1
fi

echo $(date)" **** Data downloaded successfully **** " >> $LOGFILE

#saves analysis into daily_report.csv
python3 analyse.py >> $LOGFILE 2>&1

echo $(date)" **** Analysis complete **** " >> $LOGFILE


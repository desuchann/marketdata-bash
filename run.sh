#!/bin/bash

source config.sh

echo "$(date) **** Market monitor started **** " >> "$LOGFILE"
echo "" >> "$LOGFILE"

if [ ! -f "$RAWFILE" ]; then
    if wget -O "$RAWFILE" --append-output="$LOGFILE" "$URL1"; then
	    echo "$(date) **** Using primary API key **** " >> "$LOGFILE"

	elif wget -O "$RAWFILE" --append-output="$LOGFILE" "$URL2"; then
	    echo "$(date) **** Using backup key **** " >> "$LOGFILE"
	    
	else
	    echo "$(date) **** Both primary and backup API key urls failed **** " >> "$LOGFILE"
	    exit 1
	fi
fi

echo "$(date) **** Raw data available **** " >> "$LOGFILE"

# saves analysis into csv
python3 analyse.py 2>&1 | tee -a "$LOGFILE"

if find "$PROCESSEDFILE" -type f -mmin -1 >/dev/null; then
    echo "$(date) **** Summary csv saved **** " >> "$LOGFILE"
fi

echo "" >> "$LOGFILE"
echo "$(date) **** Analysis complete **** " >> "$LOGFILE"

echo "" >> "$LOGFILE"
echo "############################################################" >> "$LOGFILE"
echo "" >> "$LOGFILE"


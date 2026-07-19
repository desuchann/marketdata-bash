DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date)
LOGFILE="logs/monitor_$DATE.log"

URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&datatype=csv&apikey="

API_KEY=0OMWAQ5CE7E4R5AR
API_KEY_BAK=6OYREUE6BYQ4XBCK

URL1="${URL}${API_KEY}"
URL2="${URL}${API_KEY_BAK}"

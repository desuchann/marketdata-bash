DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date)

LOGFILE="logs/monitor_$DATE.log"

SYMBOL='IBM'

URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&datatype=csv&symbol="

API_KEY=0OMWAQ5CE7E4R5AR
API_KEY_BAK=6OYREUE6BYQ4XBCK

URL1="${URL}${SYMBOL}&apikey=${API_KEY}"
URL2="${URL}${SYMBOL}&apikey=${API_KEY_BAK}"

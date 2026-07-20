DATE=$(date +%Y-%m-%d)
LOGFILE="logs/monitor_${DATE}.log"
export RAWFILE="data/raw/alphavprices_${DATE}.csv"
export PROCESSEDFILE="data/processed/summary_${DATE}.csv"

export SYMBOL='IBM'
#export SYMBOL='AAPL'
#export SYMBOL='NVDA'
#export SYMBOL='NFLX'

URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&datatype=csv&symbol="

source .env

URL1="${URL}${SYMBOL}&apikey=${API_KEY}"
URL2="${URL}${SYMBOL}&apikey=${API_KEY_BAK}"

intervals = ['1s', '5s', '15s', '30s', '1m']
outlier_param = {'1s':0.01,'5s':0.03,'15s':0.05,'30s':0.06,'1m':0.07,'5m':0.10}
pairs_of_interest = ['USDT'] # Other options include 'BTC' , 'ETH'
watchlist = []  # E.g. ['ADAUSDT', 'ETHUSDT'] # Note that if watchlist has pairs, ONLY pairs in watchlist will be monitored
FUTURE_ENABLED=False # Determine whether to look at future markets
DUMP_ENABLED = True # Determine whether to look at DUMP
MIN_ALERT_INTERVAL = '15s' # Minimum interval between alerts for SAME pair
RESET_INTERVAL = '3h' # Interval for clearing array to prevent MEM ERROR
PRINT_DEBUG = True # If false we do not print messages

# Used for telegram bot updates
token = ''  # Insert token obtained from @BotFather here
chat_id = 0  # Refer to chatid
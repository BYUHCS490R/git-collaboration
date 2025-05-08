       import logging
       import os
       import pytz
       from datetime import datetime
       import alpaca_trade_api as tradeapi
       from KeyInfo import *

       # Create logs directory if it doesn't exist
       if not os.path.exists('logs'):
           os.makedirs('logs')

       # Create a formatter that uses Eastern Time
       class ETFormatter(logging.Formatter):
           """Formatter that uses Eastern Time"""

           def converter(self, timestamp):
               dt = datetime.fromtimestamp(timestamp)
               eastern = pytz.timezone('US/Eastern')
               return dt.astimezone(eastern)

           def formatTime(self, record, datefmt=None):
               dt = self.converter(record.created)
               if datefmt:
                   return dt.strftime(datefmt)
               return dt.strftime('%Y-%m-%d %H:%M:%S ET')
class AlpacaTrader:
           def __init__(self):
               self.api = tradeapi.REST(
                   API_KEY,
                   API_SECRET,
                   BASE_URL,
                   api_version='v2'
               )
               self.symbol = SYMBOL
               self.position_size = POSITION_SIZE
               logging.info(f"Trader initialized for {self.symbol}")
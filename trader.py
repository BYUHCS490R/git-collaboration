       import logging
       import os
       import pytz
       from datetime import datetime

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
# Example configuration file. Create your own config.py using your values!
#-------------------------------------------------------------------------
# The data source can either be 'yahoo' or 'csv'
data_source = 'yahoo'

# Yahoo import settings. Please keep the first line of the file as 'Tickers'. The markets.txt file contains an example with a couple of markets.
yahoo_ticker_list = 'markets.txt'

# CSV import settings
folder_name = 'Data/'
header = None 
names=['Date', 'Open', 'High', 'Low', 'Close']
price_column = 'Close'
date_column = 'Date'

# Moving average parameters
short_ma_length = 20
long_ma_length = 80

# Test date parameters
starting_date = '2023-01-01'
ending_date = '2023-12-31'
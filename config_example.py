# Example configuration file. Create your own config.py using your values!
#-------------------------------------------------------------------------
#Relative path
folder_name = 'Data/'

# CSV import settings
header = None 
names=['Date', 'Close', 'Volume']
price_column = 'Close'
date_column = 'Date'

# Moving average parameters
short_ma_length = 20
long_ma_length = 80

# Test date parameters
starting_date = '2023-01-01'
ending_date = '2023-12-31'
import config
import pandas as pd
import os
from data_processing import process_yahoo_data, process_csv_data
from export import export_results

if config.data_source == 'yahoo':
    tickers = pd.read_csv(config.yahoo_ticker_list)['Tickers'].tolist()
    results = process_yahoo_data(tickers)
elif config.data_source == 'csv':
    filenames = [f for f in os.listdir(config.folder_name) if f.endswith('.csv')]
    results = process_csv_data(filenames)
else:
    raise Exception('Please use "yahoo" or "csv" as the data source in your config file!')

df = pd.DataFrame(list(results.items()), columns=['Ticker', 'Turning Points'])
average_turning_points_count = round(df['Turning Points'].mean(), 2)

print(df)
print(f'Avg turning points count: {average_turning_points_count}')

ans = input('Would you like to export these results to a spreadsheet? [Y/N]')
if ans.lower() == 'y':
    export_results(df, average_turning_points_count)
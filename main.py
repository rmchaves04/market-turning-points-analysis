import config
import pandas as pd
import os
from data_processing import get_data, count_turning_points

csv_files = [f for f in os.listdir(config.folder_name) if f.endswith('.csv')]
results = {}

for file in csv_files:
    market_data = get_data(file)
    results[file] = count_turning_points(market_data)

df = pd.DataFrame(list(results.items()), columns=['Filename', 'Turning Points'])
average_turning_points_count = round(df['Turning Points'].mean(), 2)

print(df)
print(f'Avg turning points count: {average_turning_points_count}')
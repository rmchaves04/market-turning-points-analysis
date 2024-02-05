import config
import pandas as pd
import numpy as np

def get_data(filename):
    df = pd.read_csv(config.folder_name + filename, header=config.header, names=config.names)
    df[config.date_column] = pd.to_datetime(df[config.date_column], format='%Y%m%d')

    df['MA_Short'] = df[config.price_column].rolling(config.short_ma_length).mean()
    df['MA_Long'] = df[config.price_column].rolling(config.long_ma_length).mean()

    starting_date = pd.to_datetime(config.starting_date)
    ending_date = pd.to_datetime(config.ending_date)
    df = df[(df[config.date_column] >= starting_date) & (df[config.date_column] <= ending_date)]

    return df

def count_turning_points(df):
    df['diff'] = df['MA_Short'] - df['MA_Long']
    df['sign'] = np.sign(df['diff'])
    df['crossing'] = df['sign'].diff().abs()
    turning_points_count = df['crossing'].sum() / 2

    return int(turning_points_count)
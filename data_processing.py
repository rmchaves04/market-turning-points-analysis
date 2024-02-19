import config
import pandas as pd
import numpy as np
import yfinance as yf

def process_yahoo_data(tickers):
    results = {}

    starting_date = pd.to_datetime(config.starting_date)
    adjusted_starting_date = starting_date - pd.tseries.offsets.BDay(config.long_ma_length + 7)
    adjusted_starting_date = adjusted_starting_date.strftime('%Y-%m-%d')

    data = yf.download(tickers, adjusted_starting_date, config.ending_date)

    for ticker in tickers:
        df = data.xs(ticker, level='Ticker', axis=1).dropna()
        df.reset_index(inplace=True)
        market_data = calculate_moving_averages(df)
        results[ticker] = count_turning_points(market_data)

    return results

def process_csv_data(filenames):
    results = {}

    for file in filenames:
        df = pd.read_csv(config.folder_name + file, header=config.header, names=config.names)
        market_data = calculate_moving_averages(df)
        results[file] = count_turning_points(market_data)

    return results

def calculate_moving_averages(df):
    df = df.copy()
    df[config.date_column] = pd.to_datetime(df[config.date_column], format='%Y%m%d')

    df['MA_Short'] = df[config.price_column].rolling(config.short_ma_length).mean()
    df['MA_Long'] = df[config.price_column].rolling(config.long_ma_length).mean()

    starting_date = pd.to_datetime(config.starting_date)
    ending_date = pd.to_datetime(config.ending_date)
    df = df[(df[config.date_column] >= starting_date) & (df[config.date_column] <= ending_date)]

    return df

def count_turning_points(df):
    df = df.copy()
    df['diff'] = df['MA_Short'] - df['MA_Long']
    df['sign'] = np.sign(df['diff'])
    df['crossing'] = df['sign'].diff().abs()
    turning_points_count = df['crossing'].sum() / 2

    return int(turning_points_count)
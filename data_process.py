import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import csv

def pre_process_price(price_df):
    """
    """
    price_df.rename(columns={'Date':'date', 'Open':'open', 'Close':'close'}, inplace=True)
    price_df['date'] = price_df['date'].apply(lambda x: datetime.datetime.strptime(x, '%d-%b-%y'))
    price_df['open'] = price_df['open'].apply(lambda x: float(x.replace(',', '')))
    price_df['close'] = price_df['close'].apply(lambda x: float(x.replace(',', '')))
    res_df = price_df[['date', 'open', 'close']]
    return res_df

def pre_process_curr(news_df):
    """
    Read from cryptocurrencynews.csv
    """
    news_df['date'] = [x+'-'+y for x,y in zip(news_df['date'],news_df['year'].apply(str))]
    news_df['date'] = news_df['date'].apply(lambda x: datetime.datetime.strptime(x, '%d-%b-%Y'))
    news_df.rename(columns={'title':'text'}, inplace=True)
    return news_df

def pre_process_crypto(news_df):
    """
    Read from cryptonews.csv
    """
    news_df['date'] = news_df['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    news_df.rename(columns={'title':'text'}, inplace=True)
    return news_df

def combine_news(curr_df, crypto_df):
    """
    combine news_data set together
        args:
            curr_df(DataFrame): the processed dataset from cryptocurrency.news
            crypto_df(DataFrame): the processed dataset from cryptonews.com
        returns:
            df(DataFrame): the combined dataframe of curr_df and crypto_df
    """
    frames = [curr_df[['text','date']], crypto_df]
    newsOfBitcoin = pd.concat(frames, ignore_index=True)
    return newsOfBitcoin

def add_label(price_df):
    """
    """
    price_df['diff'] = price_df['close'] - price_df['open']
    price_df['label'] = ['Up' if x > 0 
                         else 'Down' for x in price_df['diff']]
    return price_df
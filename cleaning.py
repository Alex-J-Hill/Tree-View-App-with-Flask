import pandas as pd
import os
from datetime import datetime

#Load CSV into Pandas dataframe
df = pd.read_csv('/home/ajh/learningproj/flask-tutorial/ticketInfo.csv')
print(df.info())

#Change date format for date columns for Postgres to recognize date format upon ingestion
df['processed_date'] = pd.to_datetime(df['processed_date'], dayfirst=True)
df['processed_date'] = df['processed_date'].dt.strftime('%d/%m/%Y')

df['renegotiated_date'] = pd.to_datetime(df['renegotiated_date'], dayfirst=True)
df['renegotiated_date'] = df['renegotiated_date'].dt.strftime('%d/%m/%Y')

df['closed_date'] = pd.to_datetime(df['closed_date'], dayfirst=True)
df['closed_date'] = df['closed_date'].dt.strftime('%d/%m/%Y')

#Write cleaned dataframe to a new csv file
df.to_csv('ticketInfo_clean.csv', header=True, index=False)
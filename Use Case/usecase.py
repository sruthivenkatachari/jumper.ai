import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

def session_count(d):
  v = np.diff(list(d))
  total = 0
  count = 0
  for each in v:
      total += each
      if each>=1800:
          count+=1
          total=0
      elif total >= 1800:
          count+=1
          total=0
  if total>0:
      count+=1
  return count


####use of excel sheet####
df = pd.read_excel("C:\\Users\\sruthi\\Desktop\\USE CASE\\chatlogs_excel.xlsx", sheet_name='Chat Logs')
created = df.groupby(["created"]).size().sort_values(ascending=False)
print('\n1. when do most message occur? \n', created.head(1).index)

pointofsale = df.groupby(["pointofsale"]).size().sort_values(ascending=False)
print('\n2. which is the most popular channel of communication?\n', pointofsale.head(1))

pointofsale = df.groupby(["sender_type"]).size().sort_values(ascending=False)
print('\npointof sale: \n', pointofsale.head(1))

sessions = df[['created','User_ID']]
sessions['created'] = pd.to_datetime(sessions['created'])
sessions['total_sessions'] = sessions['created'].apply(lambda x: int(x.timestamp()))
sessions.set_index('User_ID', inplace=True)
sessions = sessions.groupby('User_ID')

sessions = sessions.agg(session_count)
print("\n3.How many sessions are there?\n",sessions['total_sessions'].sum())

df=df[df.sender_type.eq('User')]
#print(df[['User_ID']]) 
a=df['User_ID'].value_counts(ascending=True)
#print(a)
print("\n4.who is the active user?\n",a.tail(1))









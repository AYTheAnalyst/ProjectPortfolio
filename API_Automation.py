#!/usr/bin/env python
# coding: utf-8

# ## Automate API Extraction + Appending Data + Visualization

# In[14]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

#NOTE:
# I had to go in and put "jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"
# Into the Anaconda Prompt to change this to allow to pull data


    # Use this if you want to create a csv and append data to it
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df

    if not os.path.isfile(r'/Users/abhishek/Downloads/csvfiles/API.csv'):
        df.to_csv(r'/Users/abhishek/Downloads/csvfiles/API.csv', header='column_names')
    else:
        df.to_csv(r'/Users/abhishek/Downloads/csvfiles/API.csv', mode='a', header=False)
        
        
    #Then to read in the file: df = pd.read_csv(r'C:\Users\alexf\OneDrive\Documents\Python Scripts\API.csv')

# If that didn't work try using the local host URL as shown in the video


# In[15]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(5) #sleep for 5 seconds
exit()


# In[17]:


df = pd.read_csv(r'/Users/abhishek/Downloads/csvfiles/API.csv')
df


# In[18]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[19]:


df


# In[20]:


df2 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df2


# In[21]:


df3 = df2.stack()
df3


# In[22]:


df4 = df3.to_frame(name='values')
df4


# In[23]:


df4.count()


# In[25]:


#Because of how it's structured above we need to set an index. I don't want to pass a column as an index for this dataframe
#So I'm going to create a range and pass that as the dataframe. You can make this more dynamic, but I'm just going to hard code it


index = pd.Index(range(90))

# Set the above DataFrame index object as the index
# using set_index() function
df5 = df4.reset_index()
df5

# If it only has the index and values try doing reset_index like "df5.reset_index()"


# In[26]:


# Change the column name

df6 = df5.rename(columns={'level_1': 'percent_change'})
df6


# In[28]:


df6['percent_change'] = df6['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df6


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[30]:


sns.catplot(x='percent_change', y='values', hue='name', data=df6, kind='point')


# In[31]:


# Now to do something much simpler
# we are going to create a dataframe with the columns we want

df7 = df[['name','quote.USD.price','timestamp']]
df7 = df7.query("name == 'Bitcoin'")
df7


# In[32]:


sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp', y='quote.USD.price', data = df7)


# In[ ]:





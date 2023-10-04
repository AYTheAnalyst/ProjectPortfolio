#!/usr/bin/env python
# coding: utf-8

# ## Scraping Data from a Real Website + Pandas

# In[75]:


from bs4 import BeautifulSoup
import requests


# In[76]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

Page = requests.get(url)

Soup = BeautifulSoup(Page.text, 'html')

print(Soup)


# In[77]:


Soup.find('table', class_ = 'wikitable sortable' )


# In[78]:


table = Soup.find_all('table')[1]
print(table)


# In[79]:


world_titles = table.find_all('th')


# In[80]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[81]:


import pandas as pd


# In[82]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[83]:


column_data = table.find_all('tr')


# In[84]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    Length = len(df)
    df.loc[Length] = individual_row_data


# In[85]:


df


# In[90]:


df.to_csv(r'/Users/abhishek/Downloads/csvfiles/Web_Scrapping.csv', index = False)


#!/usr/bin/env python
# coding: utf-8

# ## Automated Web Scrapper for Daily Gold Price

# In[ ]:


#import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import datetime
import csv
import ssl


# Connect to website

URL = 'https://www.google.com/search?q=gold+price+today+delhi&oq=gold&gs_lcrp=EgZjaHJvbWUqEAgDEAAYgwEYkgMYsQMYgAQyDwgAEEUYORiDARixAxiABDIQCAEQABiDARixAxjJAxiABDIKCAIQABiSAxiABDIQCAMQABiDARiSAxixAxiABDINCAQQABiDARixAxiABDIQCAUQLhjHARixAxjRAxiABDIGCAYQRRg8MgYIBxBFGDzSAQg2MTcxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = (soup2.find(class_="qhJBid").get_text()).strip()

price = (soup2.find(class_="vlzY6d").get_text()).strip()

char_to_replace = {'Indian Rupee': '',' ': '','\n\n\n\n\n':'',',':''}

for key, value in char_to_replace.items():
    # Replace key character with value character in string
    price = price.replace(key, value)

nprice = float(price)
type(nprice)

today = datetime.date.today()    
    
def send_mail():   
    
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "yabhishekq23@gmail.com"
    receiver_email = "yabhishekq23@gmail.com"
    password = "brks oarl stne awbt"
    message = """\
    Subject: The Gold you want is showing a drastic change in value! Now is your chance to sell or buy!
    
Abhishek, This is the moment we have been waiting for. Now is your chance to trade in gold"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

        
def check_price():
    if(nprice < 52000.0 or nprice > 65000.0):
        send_mail()

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


header = ['Title', 'Price', 'Date']

    data = [title, nprice, today]

    with open('DailyGoldPrice.csv', 'a+', newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


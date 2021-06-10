#scraping the stock price
import requests
from bs4 import BeautifulSoup
import datetime
#import pandas as pd
import os
#import mysql.connector
import pytz
import csv



def sto_price():
    global a
    global stock_name
    global stock_price
    global n_list
    global p_list
    global dttm

    r=requests.get('https://www.morningstar.com/markets')
    html=r.content

    soup=BeautifulSoup(html,'html.parser')
    csv_file=open('scraped_stock.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Product Name','Price','Date/Time(GMT)'])

    n_list=[]
    p_list=[]
    dttm=[]


    for a in soup.find_all('td',{'class':'mdc-table-cell mds-data-table__cell mdc-table-link-cell mdc-market-indexes-table__name mdc-table-cell--truncated'}):

        stock_name = a.text
        n_list=n_list+[stock_name]
        dd=datetime.datetime.now(pytz.timezone("GMT"))
        dttm = dttm + [dd.strftime("%Y-%m-%d %H:%M:%S")]

    for b in soup.find_all('td',{'class':'mdc-table-cell mds-data-table__cell mdc-table-link-cell mdc-market-indexes-table__price mds-data-table__cell--right'}):

        stock_price=b.text
        p_list=p_list+[stock_price]
    zipped = zip(n_list, p_list, dttm)
    e = list(zipped)
    print(e)
    csv_writer.writerows(e)
    csv_file.close()


sto_price()






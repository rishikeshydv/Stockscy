#scraping the reviews of the client on hotels/restraunts
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import mysql.connector
import os
import datetime
import pytz
import csv
r=requests.get('https://www.tripadvisor.com/Tourism-g60763-New_York_City_New_York-Vacations')
html=r.content

soup=BeautifulSoup(html,'html.parser') 
#all_data1=soup.find_all('div',{'class':'ui_container'})
    

n_hotel=[]
rev=[]
dttm=[]
csv_file=open('reviews.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Firm Name','Review','Date/Time(GMT)'])


def review():
    global n_hotel
    global rev
    global dttm

    #global price_list
    #global dttm
    # print(all_data1, 'check 2')
    for x in soup.find_all('div',{'class':'_1BdZ1sPm gZ95jyA4 _38K76hiv'}):


        name=x.text
        n_hotel = n_hotel + [name]
        dd=datetime.datetime.now(pytz.timezone("GMT"))
        dttm = dttm + [dd.strftime("%Y-%m-%d %H:%M:%S")]
        
    for y in soup.find_all('span',{'class':'_1KK223I5'}):

        r = y.text
        rev = rev + [r]
        #print(price_list)
    zipped = zip(n_hotel, rev, dttm)
    d = list(zipped)
    print(d)
    csv_writer.writerows(d)
    csv_file.close()


review()






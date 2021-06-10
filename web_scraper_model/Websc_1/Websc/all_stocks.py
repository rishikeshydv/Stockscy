import requests
import pytz
from bs4 import BeautifulSoup
import datetime
import os
import csv
#import pdb

class total_stock:

    global a_price
    global soup
    r = requests.get('https://robinhood.com/collections/technology')
    html = r.content
    soup = BeautifulSoup(html,'html.parser')

    def __init__(self):

        self.k = None

    def backgd(self):

        global csv_writer, csv_file

        csv_file=open('scraped.csv','w')
        csv_writer=csv.writer(csv_file)
        csv_writer.writerow(['Product Name','Symbol','Price','Today','Market Capital','Date/Time(GMT)'])
        return csv_writer, csv_file


      
    def nam_date_time(self): 
        #global soup
        global name_list, dttm
        global indx
        r=requests.get('https://robinhood.com/collections/technology')
        html=r.content
        soup = BeautifulSoup(html,'html.parser')      

        name_list = [] 
        dttm = []
        
        
        for n in soup.find_all('span',{'class':'_2fMBL180hIqVoxOuNVJgST'})[:]:
            
            name = n.text
            name_list = name_list + [name]
            indx = len(name_list)
            dd = datetime.datetime.now(pytz.timezone("GMT"))
            dttm = dttm + [dd.strftime("%Y-%m-%d %H:%M:%S")]

        return name_list, dttm
            

    def price(self): 
        
        global price_list
        price_list = []

        for p in soup.find_all('a',{'class':'rh-hyperlink'})[2::+6]:

            a_price = p.text
            price_list = price_list + [a_price]

        return price_list
            
    def symbol(self):

        global symb

        symb = []

        
        for q in soup.find_all('a',{'class':'rh-hyperlink'})[1::+6]:

            sym = q.text
            symb = symb + [sym]

        return symb

    def market_capital(self):
        
        global mc
        mc = []
        
        for r in soup.find_all('a',{'class':'rh-hyperlink'})[4::+6]:

            cap = r.text
            mc = mc + [cap] 

        return mc

    def csv_making(self, name_list, symb, price_list, mc, dttm, csv_writer):

        zipped = zip(name_list, symb, price_list, mc, dttm)
        d = list(zipped)
        print(d)
        csv_writer.writerows(d)
        #csv_file.close()
        return len(d), d
    
e = total_stock()
e.backgd()
e.nam_date_time()
e.symbol()
e.price()
e.market_capital()
e.csv_making(name_list, symb, price_list, mc, dttm,csv_writer)










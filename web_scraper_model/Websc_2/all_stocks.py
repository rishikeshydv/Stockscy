import requests
import pytz
from bs4 import BeautifulSoup
import datetime
import os
import csv
#import pdb

class total_stock:

    global indx
    global soup
    #indx = None
    r = requests.get('https://robinhood.com/collections/technology')
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    
    def __init__(self):

        self.k = None
        
    def nam(self): 
    
        
        name_list = [] 
        
        for n in soup.find_all('span',{'class':'_2fMBL180hIqVoxOuNVJgST'})[:]:
            
            name = n.text
            name_list = name_list + [name]
            indx = len(name_list)
              
        return name_list

    def get_index(self, indx):

        self.indx = indx

        return self.indx

    def date_time(self):
        
        dttm = []

        for a in range(100):
            dd = datetime.datetime.now(pytz.timezone("GMT"))
            dttm = dttm + [dd.strftime("%Y%m%d.%H%M%S")]

        return dttm
            

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
        
        for r in soup.find_all('a', {'class': 'rh-hyperlink'})[4::+6]:

            cap = r.text
            mc = mc + [cap] 

        return mc










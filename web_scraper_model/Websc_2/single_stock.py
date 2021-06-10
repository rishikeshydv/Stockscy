#New York Stack Exchange
import requests
import pytz
from bs4 import BeautifulSoup
import datetime
import csv




class individual_stock:

    global price_list
    global dm
    global indx
    global soup
    global i, j, k, l

    r = requests.get('https://robinhood.com/collections/technology')
    html = r.content
    soup = BeautifulSoup(html,'html.parser')

    def __init__(self):
        self.p=None

    def nam(self,j):
        nam_list = []

        for w in soup.find_all('a', {'class': 'rh-hyperlink'})[j]:

            stock_name = w.text
            nam_list = nam_list + [stock_name]
                    
        return nam_list

         
    def price(self, i):
        #global i
        price_list = []
        

        for p in soup.find_all('a', {'class': 'rh-hyperlink'})[i]:

            a_price = p.text
            a_price = a_price.replace('$', '')
            price_list.append(a_price)
                    
        return price_list

    def date_time(self):
        
        dm = []

        for a in range(1):
            dd = datetime.datetime.now(pytz.timezone("GMT"))
            dd = dd.strftime("%Y%m%d.%H%M%S")
            dm.append(dd)

        return dm
            

            
    def symbol(self,k):

        global symb

        symb = []

        
        for q in soup.find_all('a',{'class':'rh-hyperlink'})[k]:

            sym = q.text
            symb = symb + [sym]

        return symb

    def market_capital(self,l):
        
        global mc
        mc = []
        
        for r in soup.find_all('a',{'class':'rh-hyperlink'})[l]:

            cap = r.text
            #cap = cap.replace('M','').replace('B','')
            mc.append(cap)

        return mc 

            


        









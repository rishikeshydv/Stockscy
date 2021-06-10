#New York Stack Exchange
import requests
import pytz
from bs4 import BeautifulSoup
import datetime
import csv


class individual_stock:

    global price_list
    global dm
    global r, html, soup, csv_file, csv_writer

    r = requests.get('https://robinhood.com/collections/technology')
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
       
    csv_file=open(str(i)+'.csv','a')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Price','Date'])

    def __init__(self):
        self.p=None
         
    def price_with_time(self, i):
        #global i
        price_list = []
        dm = []

        for p in soup.find_all('a', {'class': 'rh-hyperlink'})[i]:

            a_price = p.text
            a_price = a_price.replace('$', '')
            dd = datetime.datetime.now(pytz.timezone("GMT"))
            dd = dd.strftime("%Y%m%d-%H%M%S")
            price_list.append(a_price)
            dm.append(dd)

        
        return price_list, dm
            
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
               
        
    def csv_writing(self):

        zipped = zip(price_list,dm)
        d = list(zipped)
        print(d)
        csv_writer.writerows(d)
        csv_file.close()
            
        return csv_file

f=individual_stock()
print(f.price_with_time(2))


        









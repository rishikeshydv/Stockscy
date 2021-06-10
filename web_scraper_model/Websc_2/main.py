import requests
from bs4 import BeautifulSoup
import pandas as pd
from all_stocks import total_stock
from single_stock import individual_stock
from Plt import plots
import csv
ind_st = individual_stock()
ts = total_stock()
plt = plots()
# ########################  TOTAL STOCK    ##############################                                                           
name = ts.nam()
price = ts.price()
sy = ts.symbol()
mar = ts.market_capital()
d_t = ts.date_time()

index = name.index('Microsoft')
########################################################################

####################INDIVIDUAL STOCK####################################
j = (0+index*6) # NAME
k = (1+index*6) # SYMBOL
i = (2+index*6) # PRICE
l = (4+index*6) # MARKET CAPITAL
# NO INDEX FOR DATETIME
# +6 to go to next STOCK

individual_name = ind_st.nam(j)
individual_price = ind_st.price(i)
individual_symbol = ind_st.symbol(k)
individual_market = ind_st.market_capital(4)
individual_date = ind_st.date_time()
#print(individual_name, individual_price)
########################################################################

###############   APPEND in the CSV file   ############################################

#csv_file=open('stock.csv','a')
#csv_writer=csv.writer(csv_file)
#csv_writer.writerow(['Price','Date'])

########################################################################


#################################  BACKGROUND TASKS   ###############################
r = requests.get('https://robinhood.com/collections/technology')
html = r.content
soup = BeautifulSoup(html,'html.parser')
#####################################################################################

################################# CSV FILE MAKING ###################################
csv_file = open('total_stock.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Price','Date'])

zipped = zip(name,price,d_t)
d = list(zipped)
print(d)
csv_writer.writerows(d)
csv_file.close()
######################################################################################

#################################  GRAPH PLOT  ##############################################
df = pd.read_csv('Catalyst Pharmaceuticals Monthly.csv')
title = 'Scatter Plot' 
ylab = 'Price($)'             #xlabel of the plot
xlab = 'Date(GMT)'             #ylabel of the plot
#x = df.Date                  # x coordinate             
#y = df.Price               # y coordinate

#print(plt.scatter_plot(df, title, xlab, ylab, x, y))  #--> Displays the ScatterPlot
#print(plt.line_graph(df, title, xlab, ylab, x, y))    #--> Displays the LineGraph
#############################################################################################


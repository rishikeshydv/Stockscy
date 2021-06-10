import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pdb

def scatter_plot(i):

    try:
        df=pd.read_csv(str(i)+'.csv')
    except:
        print('Corresponding index hasnt been scraped yet')
        
    #df.plot(kind='scatter',x='Date/Time(GMT)',y='Price',color='black')
    #plt.xticks(rotation=45)
    plt.title('Stock Price')
    #plt.xticks(rotation=45)
    plt.xlabel('Date/Time(GMT)(YYMMDD-HHMMSS)')
    plt.ylabel('Price($)')
    #pdb.set_trace()
    print(df,'Check1')
    x = (df.Date)
    

    y = (df.Price)
    plt.xticks(rotation=45)
    plt.scatter(x,y)
    plt.show()
    return

def line_graph():

    file = pd.read_csv('Catalyst Pharmaceuticals Monthly.csv')
    plt.figure(figsize=(20,25))
    plt.plot(file.Date, file.Price, 'r.-')
    plt.title('Stock Price of PC with DT(GMT) - New York Stack Exchange')
    plt.xticks(rotation=45)
    plt.xlabel('Date/Time(GMT)(YYMMDD-HHMMSS)')
    plt.ylabel('Price($)')
    plt.show()
    #plt.xticks(file.Date[::3])
    plt.legend() 
    return



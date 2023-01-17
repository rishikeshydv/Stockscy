import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pdb

class plots:

    def scatter_plot(self, df, title, xlab, ylab, x, y):

        
        plt.title(title)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.xticks(rotation=45)
        plt.scatter(x, y)
        plt.show()
        return 

    def line_graph(self, df, title, xlab, ylab, x, y):

        plt.figure(figsize=(20,25))
        plt.plot(x, y, 'r.-')
        plt.title(title)
        plt.xticks(rotation=45)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.show()
        #plt.xticks(file.Date[::3])
        plt.legend() 
        return 


Stockscy is a versatile data scraping tool that pulls individual and bulk stock data from Robinhood, Yahoo Finance and others
Added additional features to graphically showcase the market values via Matplotlib and analyze them. 

Technologies used: Python, Numpy, Pandas, Matplotlib

single_stock.py scrapes individual stock and its other features from the destination website whereas all_stocks.py scrapes total stocks and their other features from the destination website. Plt.py gives visual representatio of the scraped data.

main.py imports single_stock.py and all_stocks.py and functions as the controller of the system.

The output files have .csv extensions and can be used to visually portray via Plt.py

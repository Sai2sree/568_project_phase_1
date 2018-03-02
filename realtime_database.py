realtime

import sys
import pandas as pd
import pdb
from pymongo import MongoClient
import json
from googlefinance.client import get_price_data

# stock collection using pandas into csv
class realtime_stock_data:

    def __init__(self):

        self.period = "1m"
        self.interval = 0
        self.stock_data = None 

        self.params = [
        # Verizon
        {
            'q': "VZ",
            'x': "NYSE",
            'p': self.period,
            'i': self.interval,},
        # Apple
        {
            'q': "AAPL",
            'x': "NASDAQ",
            'p': self.period,
             'i': self.interval,},
        # IBM
        {
            'q': "IBM",
            'x': "NYSE",
            'p': self.period,
            'i': self.interval,},
        # Tesla
        {
            'q': "TSLA",
            'x': "NASDAQ",
            'p': self.period,
            'i': self.interval,},
        # Pfizer
         {
            'q':'PFE',
            'x':'NYSE',
            'p': self.period,
            'i': self.interval,},

        # Starbucks 

         {
            'q':'SBUX',
            'x':'NASDAQ',
            'p': self.period,
            'i': self.interval,},

        # NIKE
        {
            'q':'NKE',
            'x':'NYSE',
            'p': self.period,
            'i': self.interval,},

        # Fiat Chrysler Automobiles NV

        {
            'q':'FCAU',
            'x':'NYSE',
            'p': self.period,
            'i': self.interval,},
        
        # Twitter Inc

        {

            'q':'TWTR',
            'x':'NYSE',
            'p': self.period,
            'i': self.interval,},

        # Toronto-Dominion Bank

        { 
            'q':'TD',
            'x':'NYSE',
            'p': self.period,
            'i': self.interval,},
        ]

        
    def store_databases(self):

        # specify client using URI
        # specify database --> mongo_client['stocks']
        # create a collection i.e. table for each stock
        
        # URI: mongodb://user:user@ds151508.mlab.com:51508/realtime_database
        
        connection = MongoClient('mongodb://user:user@ds151508.mlab.com:51508/realtime_database')

        db = connection['realtime_databse']
        db.authenticate('user', 'user')

        
        for param in self.params:
            # collection for each stock
            db_collection = db['{}'.format(param['q'])] 

            ## Insert stock data as documents in a collection 

            _stock_data = get_price_data(param)
            print _stock_data
            db_collection.insert_many(_stock_data.to_dict('records'))



if __name__ == "__main__":

    realtime_stocks = realtime_stock_data()
    realtime_stocks.store_databases()






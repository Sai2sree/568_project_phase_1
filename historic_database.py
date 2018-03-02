import sys
import pandas as pd
import pdb
from pymongo import MongoClient
import json
from googlefinance.client import get_price_data

# stock collection using pandas into csv
class historic_stock_data:

    def __init__(self):

        self.period = "1Y"
        self.interval = 60
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


        # Google

        {
            'q':'GOOGL',
            'x':'NASDAQ',
            'p': self.period,
            'i': self.interval,},
        
        ]

        
    def store_databases(self):

        # specify client using URI
        # specify database --> mongo_client['stocks']
        # create a collection i.e. table for each stock
        
        # URI: mongodb://user:usingser@ds027729.mlab.com:27729/historic_database

        connection = MongoClient('mongodb://user:user@ds027729.mlab.com:27729/historic_database')

        db = connection['historic_database']
        db.authenticate('user', 'user')

        
        for param in self.params:
            # collection for each stock
            db_collection = db['{}'.format(param['q'])] 

            ## Insert stock data as documents in a collection 

            _stock_data = get_price_data(param)
            print _stock_data
            db_collection.insert_many(_stock_data.to_dict('records'))



if __name__ == "__main__":

    historic_stocks = historic_stock_data()
    historic_stocks.store_databases()






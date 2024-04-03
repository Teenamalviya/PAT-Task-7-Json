import json
import re
from urllib import response
from urllib.request import urlopen
import requests



class JSONProject:

    # parameterized constructor
    def __init__(self, url):
        self.url = url


    # Fetch JSON data from the url
    def fetch_data(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data

    # Method for displaying countries with name, currencies and its symbols.
    def display_countries_with_name_currencies_symbols(self):
        jsondata = self.fetch_data()
        country_c = {}
        country_list = []
        currency_list = []

        #Iterating over Json Data
        for name_data in jsondata:
            name = name_data["name"]["common"]
            currency_dict = name_data.get('currencies', {})
            currency_keys = list(name_data.get('currencies', {}).keys())

            for a in currency_keys:
                country_currency = a
                currency_name = currency_dict.get(a, {}).get('name')
                symbol = currency_dict.get(a,{}).get('symbol')
                country_list.append(name)
                currency_list.append(currency_name)
            print("Country: ",name, "Currency: ",country_currency, "Symbol: ", symbol)

        # Create Dictionary to send country names and its currency name
        country_c = {country_list[i]: currency_list[i] for i in range(len(country_list))}
        return country_c

    # Method to display countries with currency as dollars
    def display_countries_currencies_as_dollars(self):
        c= self.display_countries_with_name_currencies_symbols()
        prefix = "dollar"
        dollar_dict = {k for k, v in c.items() if prefix in v}
        print("Countries with Dollar as currency:", dollar_dict)

    # Method to display countries with currency as euros
    def display_countries_currencies_as_euros(self):
        c = self.display_countries_with_name_currencies_symbols()
        prefix = "Euro"
        euro_dict = {k for k, v in c.items() if prefix in v}
        print("Countries with Euros as currency: ", euro_dict)

#Create JSONProject object
jsonobj = JSONProject("https://restcountries.com/v3.1/all")
# Calling JSon Fetch Method
jsonobj.fetch_data()
# Calling method  to display countries with currencies and its symbols
jsonobj.display_countries_with_name_currencies_symbols()
# Calling method to display countries with currency as dollars
jsonobj.display_countries_currencies_as_dollars()
# Calling method to display countries with currency as euros
jsonobj.display_countries_currencies_as_euros()

import json
import requests
from urllib import response
from urllib.request import urlopen


''''''
class OpenBrewies:

    # parameterized constructor
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        json_data = json.loads(response.text)
        #print("JSON data type:", json_data)
        return json_data

    def brewieslist(self):
        json_data = self.fetch_data()
        filtered_states_Alaska = [name_data for name_data in json_data if name_data["state_province"] == "Alaska"]
        filtered_states_Maime = [name_data for name_data in json_data if name_data["state_province"] == "Miame"]
        filtered_states_NewYork = [name_data for name_data in json_data if name_data["state_province"] == "New York"]

       # print("Alaska: ", filtered_states_Alaska)
        #print("Maime: ", filtered_states_Maime)
        #print("New_York", filtered_states_NewYork)

        #print("Number of Brewies in Alaska:", len(filtered_states_Alaska))
       # print("Number of Brewies in Alaska:", len(filtered_states_Maime))
        #print("Number of Brewies in Alaska:", len(filtered_states_NewYork))
        return filtered_states_Alaska,filtered_states_Maime,filtered_states_NewYork

    def brewies_in_ciies(self):
        filtered_states_Alaska, filtered_states_Maime, filtered_states_NewYork = self.brewieslist()
        brewciity_list = [filtered_states_Alaska, filtered_states_Maime, filtered_states_NewYork]
        for bc in brewciity_list:
            breweies_type = {}
            brew_list = []
            city_list = []
            website_list = []
            state_list = []
            for item in bc:
                #print("State:",(item['state_province']) )
                website_list.append(item['website_url'])
                brew_list.append(item['brewery_type'])
                city_list.append(item['city'])
                state_list.append(item['state_province'])
            breweies_type = list(map(lambda a, b, c, d:(a,b,c,d), state_list, city_list, brew_list, website_list))

            brewtype = list(set([lis[2] for lis in breweies_type]))
            print(brewtype)

            #print("Number of Breweries having websites:",len(website_list))


#Create JSONProject object
openBrew = OpenBrewies("https://api.openbrewerydb.org/v1/breweries")
openBrew.fetch_data()
openBrew.brewieslist()
openBrew.brewies_in_ciies()



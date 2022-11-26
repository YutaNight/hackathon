import requests
import json

class ResasInfo:
    API_KEY = 'ad5czQs0Y5B2yxp8i8u9FNeAPUmdGf6LZgrQBiNY'
    
    def __init__(self, pref_code):
        self.pref_code = pref_code
        self.url = 'https://opendata.resas-portal.go.jp/api/v1/cities?prefCode={}'.format(pref_code)
        self.headers = {
            'x-api-key': 'ad5czQs0Y5B2yxp8i8u9FNeAPUmdGf6LZgrQBiNY'
        }
    
    def get_cities_data(self, city_name):
        res = requests.get(self.url, headers=self.headers)
        res_data_list = json.loads(res.text)['result']
        return [data for data in res_data_list if data['cityName'] == city_name][0]['bigCityFlag']
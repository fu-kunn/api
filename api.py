# import requests
# import os
# from dotenv import load_dotenv
# import pandas as pd

# load_dotenv('.env')

# URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
# API_KEY = os.environ.get('KEY')
# params = {
#   'key': API_KEY,
#   'keyword': '沖縄',
#   'format': 'json',
#   'count': 100
# }

# res = requests.get(URL, params)
# result = res.json()
# items = result['results']['shop']
# df = pd.DataFrame(items)
# df = df[['name', 'address', 'wifi']]
# df.to_csv('hotpepper.csv', index=False)
# print(df.head())
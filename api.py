import requests

import os
from dotenv import load_dotenv

load_dotenv('.env')

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
API_KEY = os.environ.get('KEY')
params = {
  'key': API_KEY,
  'keyword': '沖縄',
  'format': 'json'
}

res = requests.get(URL, params)
result = res.json()
print(result['results'])
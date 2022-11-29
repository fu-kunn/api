import requests
import pandas as pd
REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = '1096144112853963195'

params = {
  'applicationId': APP_ID,
  'format': 'json',
  'keyword': 'バスローブ',
  'minPrice': 10000
}

res = requests.get(REQUEST_URL, params)
print(res.status_code)

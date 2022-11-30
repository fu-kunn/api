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
result = res.json()
items = result['Items']
items = [item['Item'] for item in items]
df = pd.DataFrame(items)

columns = ['itemName', 'shopName', 'itemPrice', 'availability']
df = df[columns]
new_columns = ['商品名', '店名', '商品価格', '販売可']
df.columns = new_columns
# print(df.dtypes)
print(df.sort_values('商品価格', ascending = False))
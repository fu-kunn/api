import gspread
import pandas as pd

from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

# 定数の宣言
SP_SHEET_KEY = '1d-u9f8WqlWXlsbYXTDgLkNN4M2CofoVn022Ka2OTMl4'
# https://docs.google.com/spreadsheets/d/1d-u9f8WqlWXlsbYXTDgLkNN4M2CofoVn022Ka2OTMl4/edit#gid=0
SP_SHEET = 'demo'

# スプシ全体の読み込み
sh = gc.open_by_key(SP_SHEET_KEY)
# スプシ単体の読み込み
worksheet = sh.worksheet(SP_SHEET)
data = worksheet.get_all_values()
df = pd.DataFrame(data[2:], columns=data[1])
df = df.drop(df.columns[[0]], axis=1)
# 縦横のカラム数を返す
test = df.shape
# print(df)
print(test)

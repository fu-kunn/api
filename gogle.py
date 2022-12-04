import gspread

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

# スプシの読み込み
sh = gc.open_by_key(SP_SHEET_KEY)
print(sh)

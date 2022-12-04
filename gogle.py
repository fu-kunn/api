import gspread
import pandas as pd

from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

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
# １列目の余白を削除
df = df.drop(df.columns[[0]], axis=1)
# 縦横のカラム数を返す
test = df.shape
# print(test)

"""
所属毎の年齢を算出する方法
"""
# データ型の変換object→int
df = df.astype({'年齢': int, '社員ID': int})
# mean=平均
pvt_table = df.pivot_table(index=['所属'], values=['年齢'], aggfunc='mean')
# 少数の丸め込み
pvt_table = pvt_table['年齢'].round()

# スプシに新規のタブを追加
new_worksheet = sh.add_worksheet(title='new', rows=100, cols=100)

first_row = 2
first_col = 2
set_with_dataframe(new_worksheet, pvt_table.reset_index(), row=first_row, col=first_col)


# print(new_worksheet)

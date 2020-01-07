import pandas as pd

file = '/Users/apple/desktop/py4e/importData1/battledeath.xlsx'

xls=pd.ExcelFile(file)

#for spreahsheet name
print(xls.sheet_names)

#LOADING spreadsheet using parse()
df1 = xls.parse('2002')
print(df1.head())
df1 = xls.parse(0, skiprows=[0], names=['Country', "AAM due to War (2002)"])
print(df1.head())
df2=xls.parse(1,usecols=[0], skiprows=[0],names=['Country'])
print(df2.head())

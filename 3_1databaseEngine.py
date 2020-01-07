from sqlalchemy import create_engine
import pandas as pd

# NOTE: because of using sqlite, we use 3 ///
engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')

table_name = engine.table_names()
print(table_name)

#open engine connection
con = engine.connect()

rs= engine.execute('SELECT  * FROM Album')
#fetchall() will take all the row
df= pd.DataFrame(rs.fetchall())

#close connection
#con.close()

print(df.head())

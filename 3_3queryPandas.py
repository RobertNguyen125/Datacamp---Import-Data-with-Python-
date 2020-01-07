from sqlalchemy import create_engine
import pandas as pd

#1: compare pandas and engine context manager
engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')
#use pandas to query directly
df = pd.read_sql_query("SELECT * FROM Album",engine)
print(df.head())

#open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1=pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

#confirm if the two methods yield the same result
print(df.equals(df1))

#2: More complex query
engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate',engine)
print(df.head())

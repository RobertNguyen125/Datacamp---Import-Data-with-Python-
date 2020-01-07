from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')
with engine.connect() as con:
    rs =con.execute('SELECT Lastname, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()# NOTE: for the columns title

print(len(df))
print(df.head())

#filtering using WHERE
engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')
with engine.connect() as con:
    rs =con.execute('SELECT * FROM Employee WHERE EmployeeId >=6')
    df = pd.DataFrame(rs.fetchall())
    df.columns=rs.keys()

print(df.head())

from sqlalchemy import create_engine
import pandas as pd
#create engine
engine = create_engine('sqlite:////Users/apple/desktop/py4e/ImportData1/Chinook.sqlite.txt')
#perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())

#2: filtering Inner JOIN
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackID = Track.TrackID WHERE Milliseconds<250000',engine)
print(df.head())

# In class example(s)

## November 17, 2023 

```python 
import duckdb
con = duckdb.connect('music.db')
# Run Once to Create the Artists and Albums Tables
""" 
strArtist = 'create or replace table artists(id integer primary key, band varchar(100))'
con.sql(strArtist)
strAlbums = 'create or replace table albums(id integer primary key, artist_id integer, albumname varchar(100), FOREIGN KEY (artist_id) references artists(id))'
con.sql(strAlbums)
"""
# Run Once to Add data into the Tables
""" add data
insertArtist = 'insert into artists(id, band) values(1,\'Beatles\'),(2,\'Pink Floyd\'),(3,\'Grateful Dead\'),(4,\'Queen\')'
insertAlbum = 'insert into albums(id,artist_id,albumname) values(1,1,\'The White\'),(2,1,\'Rubber Soul\'),(3,2,\'Meddle\'),(4,2,\'The Wall\'),(5,2,\'Animals\'),(6,3,\'American Beauty\'),(7,3,\'One from the Vault\'),(8,3,\'Reckoning\')'
con.sql(insertAlbum)
"""
def showrecordset():
    strJoinTbls = 'select artists.band, albums.albumname from albums, artists where artists.id = albums.artist_id'
    rs = con.sql(strJoinTbls)
    rs.show()

showrecordset()

con.close()
```

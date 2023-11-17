# SQL Start 

## CREATE (C - Create)
```sql
/* {} - insert your parameters */
/*
Create using a column name and column type in the following format:
my_column_string varchar(100),
my_column_integer integer,
my_column_text text

note the ; at the end of the SQL Statement
*/
create table {TABLENAME}(id integer primary key,
{YOUR_COLUMN} {COLUMN_TYPE},
{YOUR_COLUMN} {COLUMN_TYPE},
{YOUR_COLUMN} {COLUMN_TYPE});
create sequence {TABLENAME}_sequence start 1;
```

## SELECT (R - Review)
### All records
```sql
/* {} - insert your parameters */
select * from {TABLENAME};
```
### Only certain records
```sql
select {YOUR_COLUMN},{YOUR_COLUMN},{YOUR_COLUMN} from {TABLENAME};
```

## INSERT (U - Update) 
```sql
/* {} - insert your parameters */
insert into {TABLENAME}({YOUR_COLUMN},{YOUR_COLUMN},{YOUR_COLUMN}) VALUES('YOUR_NEW_DATA','YOUR_NEW_DATA','YOUR_NEW_DATA');
```

## UPDATE (U - Update) 
```sql
/* {} - insert your parameters */

update {TABLENAME}
set {YOUR_COLUMN} = 'YOUR_NEW_DATA'
where id = {REFERENCE_ID};
```

## DELETE (D - Delete) 
```sql
/* {} - insert your parameters */

delete from  {TABLENAME}
where id = {REFERENCE_ID};
```
# Putting the pieces together 
## Music Appreciation Database 

```python 
import duckdb
 
con = duckdb.connect('music.db')

def runsqlcmd(my_sqlstr):
    con.sql(my_sqlstr)

def showrecords(my_strSQL):
    rs = con.sql(my_strSQL)
    rs.show()

# C in CRUD == CREATE
strSQL = 'create or replace table artists(id integer primary key, band varchar(100))'
runsqlcmd(strSQL)
runsqlcmd('create or replace sequence artistsid start 1')

print("Empty table")
print("-------------------------")
# R in CRUD == Review
strSQL = 'select * from artists'
showrecords(strSQL)

# U in CRUD == UPDATE / INSERT
myinserts=[]
myinserts.append('insert into artists(id,band) values(nextval(\'artistsid\'),\'Beatles\')')
myinserts.append('insert into artists(id,band) values(nextval(\'artistsid\'),\'Queen\')')
myinserts.append('insert into artists(id,band) values(nextval(\'artistsid\'),\'Tool\')')
for i in myinserts:
    runsqlcmd(i)

print("Records in Artists Table")
print("-------------------------")
# R in CRUD == Review
strSQL = 'select * from artists'
showrecords(strSQL)
 
# U in CRUD == UPDATE
con.sql('update artists set band=\'The Who\' where id=3')
 
print("Updated records in Artists Table")
print("-------------------------")
# R in CRUD == Review
strSQL = 'select * from artists'
showrecords(strSQL)

strSQL = 'create or replace table albums(id integer primary key, artist_id integer, albumname varchar(100), FOREIGN KEY (artist_id) references artists(id))'
runsqlcmd(strSQL)
runsqlcmd('create or replace sequence albumid start 1')
print("Records in Albums Table")
print("-------------------------")
# R in CRUD == Review
strSQL = 'select * from albums'
showrecords(strSQL)
 
myinserts2=[]
myinserts2.append('insert into albums(id,artist_id,albumname) values(nextval(\'albumid\'),1,\'White Album\')')
myinserts2.append('insert into albums(id,artist_id,albumname) values(nextval(\'albumid\'),1,\'Rubber Soul\')')
myinserts2.append('insert into albums(id,artist_id,albumname) values(nextval(\'albumid\'),1,\'Yellow Sub\')')
myinserts2.append('insert into albums(id,artist_id,albumname) values(nextval(\'albumid\'),3,\'Whos Next\')')
for i in myinserts2:
    runsqlcmd(i)

print("Joined Tables")
print("-------------------------")
# R in CRUD == Review
strSQL = 'select artists.band,albums.albumname from artists, albums where artists.id=albums.artist_id'
showrecords(strSQL)

print("Filtered Table")
# rs_strSQL = 'select artists.band,albums.albumname from artists, albums where artists.id=albums.artist_id'
strSQL = 'select artists.band,albums.albumname from artists, albums where albums.albumname like \'%Soul%\' and artists.id=albums.artist_id'
showrecords(strSQL)
 
 
con.close()

```
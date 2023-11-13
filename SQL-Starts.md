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

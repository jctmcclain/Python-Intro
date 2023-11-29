# Navigator

* [Python Introduction](https://github.com/jctmcclain/Python-Intro/blob/main/python-intro.md)
* [Python Files](https://github.com/jctmcclain/Python-Intro/blob/main/FILES/python-files.md)
* [DuckDB - SQL](https://github.com/jctmcclain/Python-Intro/blob/main/SQL/SQL-Starts.md)
----
* [Swimming App](https://github.com/jctmcclain/Python-Intro/blob/main/swimmingapp/README.md)

----
* [Git - Software Code Management Tool](https://github.com/jctmcclain/Python-Intro/blob/main/GIT/GettingGit.md)

---
# PANDA Promise 

## Pandas with DuckDB

```python
import duckdb
import pandas as pd


# use duckdb to open the csv data set
# with the recordset convert to a pandas dataframe called prs

prs = duckdb.query("SELECT * from 'christmas_movies.csv'").to_df()


# with the prs data frame group by the movie rating 
# use the aggregate count function to count the number of movie ratings

print(prs.groupby(['rating']).agg(Count=('rating','count')))
```

## Pandas and Coffee

***Using a Dictionary***

```python
import pandas as pd
drinks = ({
        'Drink':['Coffee','Mocha','Latte','Cappuccino'],
        'Descript':['Brewed - Bean + Water','Brewed - Bean + Water + Chocolate + Milk','Steamed - Bean + Frothed Milk','Steamed - Bean + Frothed Milk'],
        'Cost':['1.95','2.75','3.00','3.50']})
df = pd.DataFrame(drinks, columns=['Drink','Descript','Cost'])
# Print unsorted records
print(df)
print("------------------------\n")

# Sort the records based on the column Drink
df.sort_values("Drink", inplace = True)
print(df)

# Filter the records and show only the recors with Brewed in the description
print("------------------------\n")
print("------------------------\n")
print(df[df['Descript'].str.contains('Brewed')])
```

## Pandas and Parks 

```python
import pandas as pd
df = pd.read_csv('NPDATA_202311281629.csv')
print(df)
# state_name -> State Name Listing
# area_name -> Park Name 
print ("------------------------------------------\n")
print (df.loc[:,['area_name']])
print ("------------------------------------------\n")
print ("Area Name with no duplicates\n")
print ("------------------------------------------\n")
print (df.loc[:,['area_name']].drop_duplicates())
print ("------------------------------------------\n")
print ("------------------------------------------\n")
print(df.area_name.value_counts())
print ("------------------------------------------\n")
print ("------------------------------------------\n")

# df2 = df.loc[:,['state_name','area_name']].groupby(['state_name','area_name'])['area_name'].count()
# print(df2)

df3 = df.loc[df['state_name']=='Arizona',['area_name']].drop_duplicates()
# print(df3)
# Prints out the DataFrame as a string format 
print(df3.to_string())

df4 = df.loc[df['state_name']=='Utah',['area_name']].drop_duplicates()
# Prints out the DataFrame as a string format
print(df4.to_string())
```


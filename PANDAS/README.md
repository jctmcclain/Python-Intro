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
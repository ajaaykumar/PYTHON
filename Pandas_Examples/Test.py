import pandas as pd
import pandasql as pdsql

data = pd.read_csv('/workspaces/PYTHON/Pandas_Examples/Records/Data.csv')
data = data.set_index('id')
# print(data.query("age > 40"))

sql_query = 'select * from data where age > 60'
print(pdsql.sqldf(sql_query, locals()))














































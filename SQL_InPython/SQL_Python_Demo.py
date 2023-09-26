import pyodbc
import pandas as pd
import sqlalchemy

print(pyodbc.version)

print(pyodbc.drivers())

# connecting to a database in pyodbc and sqlalchemy

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Car_2000'  # delete before uploading to github
driver = 'ODBC Driver 17 for SQL Server'

pyodbc_conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
sqlalchemy_conn = sqlalchemy.create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
cursor = pyodbc_conn.cursor()

# print(cursor)
#
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# print(row)

"""
cust_rows = cursor.execute("SELECT * FROM Customers;")  # .fetchall() returns all rows to print. Make DF require execute
print(cust_rows)

customers_df = pd.DataFrame(cust_rows)
print(customers_df)
# doesn't do it properly
"""
# pandas only supports sqlalchemy connection. must use sqlalchemy if using pandas
# sql_query = "SELECT * FROM Customers"
# df = pd.read_sql(sql_query, sqlalchemy_conn)
# print(df)

# create a dataframe straight away
paris_cus_df = pd.read_sql("SELECT * FROM Customers WHERE city = 'Paris'", con=sqlalchemy_conn)
print(paris_cus_df)

paris_cus_df.to_sql(name="paris_customers", con=sqlalchemy_conn, if_exists="replace")

query = pd.read_sql_query("SELECT * FROM paris_customers;", con=sqlalchemy_conn)
print(query)

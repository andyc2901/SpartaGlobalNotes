import pandas as pd
import sqlalchemy

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Car_2000'  # delete before uploading to github
driver = 'ODBC Driver 17 for SQL Server'

sqlalchemy_conn = sqlalchemy.create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")

customer_df = pd.read_sql("SELECT * FROM Customers", con=sqlalchemy_conn)
print(customer_df.columns)

# Check for nulls
nulls = customer_df.isnull()
# Drop row if either phone or fax is null
customer_df_no_null_PhoneFax = customer_df.dropna(subset=["Phone", "Fax"])
print(customer_df_no_null_PhoneFax)

customer_df_no_null_PhoneFax.to_sql("Customer_Phone_And_Fax", con=sqlalchemy_conn, if_exists='replace')

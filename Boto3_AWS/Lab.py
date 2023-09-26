import boto3
import pandas as pd
import io

# Load all 3 csv files as dataframes

s3_client = boto3.client('s3')
bucket_name = "data-eng-resources"

fish = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
fish_df = pd.read_csv(fish['Body'])
# print(fish_df)

fish_monday = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')
fish_tuesday = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')

fish_mon_df = pd.read_csv(fish_monday['Body'])
fish_tues_df = pd.read_csv(fish_tuesday['Body'])

# print(fish_mon_df)
# print(fish_tues_df)

# make one large dataframe with all 3 csvs joined vertically

df_montue = pd.concat([fish_mon_df, fish_tues_df])
df_all = pd.concat([fish_df, df_montue])
# print(df_all)

# There are 159 rows in each df so should be 477 in the larger table, which there are :D

# Find the average of each column grouped by species
df_avg = df_all.groupby('Species').mean()

print(df_avg)

# Write the new csv to the s3 storage on the cloud

str_buffer = io.StringIO()
df_avg.to_csv(str_buffer)
s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key='Data249/fish/Andrew.csv')
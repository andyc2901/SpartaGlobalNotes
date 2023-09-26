import boto3
import pprint as pp
import json
import pandas as pd
import io

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

bucket_list = s3_client.list_buckets()
# pp.pprint(bucket_list)
bucket_name = "data-eng-resources"
bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="big-data/Adventure Works")
# pp.pprint(bucket_contents)

bucket = s3_resource.Bucket(bucket_name)
# print(bucket)
objects = bucket.objects.all()
# print(objects)
# for obj in objects:
#     print(obj.key)

# JSONs (more unstructured)

s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')

# pp.pprint(s3_object)
# string_body = s3_object['Body'].read()
# print(string_body)
# body = json.loads(string_body)
# pp.pprint(body)

# CSVs (structured (straight to dataframe))

# s3_object2 = s3_client.get_object(Bucket=bucket_name, Key='python/happiness-2019.csv')
# pp.pprint(s3_object2)
#
# print(s3_object2['Body'].read())
#
# df = pd.read_csv(s3_object2['Body'])
# print(df)

# Creating objects

# dict_to_upload = {"name":  "data", "status": 0}
# s3_client.put_object(Body=json.dumps(dict_to_upload),
#                      Bucket=bucket_name,
#                      Key='Test249/andrew.json')
#
# s3_client.upload_file(Filename='new_json.json',
#                       Bucket=bucket_name,
#                       Key='Test249/andrew2.json')

df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
str_buffer = io.StringIO()
df.to_csv(str_buffer)
s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key='Test249/andrew.csv')

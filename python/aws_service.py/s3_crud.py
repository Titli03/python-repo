import boto3
import os
s3=boto3.resource('s3')
bucket_name='my-first-bucket-titli'
all_my_buckets=[bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print(f"'{bucket_name}' is not present, bucket creation now..")
    s3.create_bucket(Bucket=bucket_name)
    print(f"'{bucket_name}' has been created")
else:
    print(f"'{bucket_name}' is already exists")
#current_directory=os.getcwd()
#print(current_directory)
    
file1='file1.txt'
file2='file2.txt'
s3.Bucket(bucket_name).upload_file(Filename=file1, Key=file1)
obj=s3.Object(bucket_name,file1)
body=obj.get()['Body'].read()
print(body)

s3.Object(bucket_name,file1).put(Body=open(file2,'rb'))
obj=s3.Object(bucket_name,file1)
body=obj.get()['Body'].read()
print(body)

s3.Object(bucket_name,file1).delete()
s3.Bucket(bucket_name).delete()


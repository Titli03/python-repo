import csv
import boto3
from datetime import datetime

def lambda_handler(event, context):
    s3=boto3.resource('s3')
    billing_bucket=event['Records'][0]['s3']['bucket']['name']
    csv_file=event['Records'][0]['s3']['object']['key']
    error_bucket='dtc-billing-errors-2'
    
    obj=s3.Object(billing_bucket, csv_file)
    data=obj.get()['Body'].read().decode('utf-8').splitlines()
    
    error_found=False
    valid_product_lines=['Bakery','Meat','Dairy']
    valid_curencies=['USD','MXN','CAD']
    
    for row in csv.reader(data[1: ], delimiter=','):
        date=row[6]
        product_line=row[4]
        currancy=row[7]
        bill_amount=float(row[8])
        if product_line not in valid_product_lines:
            error_found=True
            print(f"Error in record {row[0]} unrecognized produc tline {product_line}")
            break
        if currancy not in valid_curencies:
            error_found=True
            print(f"Error in record {row[0]} unrecognized currancy {currancy}")
            break
        
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
           error_found=True
           print(f"error in record {row[0]} incorrect dateformat {date}")
           break 
            
    if error_found:
        copy_source={
            'Bucket': billing_bucket,
            'Key': csv_file
        }
        try:
            s3.meta.client.copy(copy_source, error_bucket, csv_file )
            print(f"move erroronus files to {error_bucket}")
            s3.Object(billing_bucket, csv_file).delete()
            print("Deleted Original file from bucket")
        except Exception as e:
            print(f"error found while data moving {str(e)}")
    else:
        return {
            'statsu code':200,
            'Body':'No Error found in the records'
        }
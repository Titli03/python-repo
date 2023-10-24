import boto3
import csv
import io
import logging
current_conversion_to_usd={'USD':1, 'CAD':0.79, 'MXN':0.05}

s3_client=boto3.client('s3')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def process_record(record):
    id, company_name, country, city, product_line, item, bill_date, currency, bill_amount=record
    bill_amount=float(bill_amount)
    
    usd_amount=0
    
    rate=current_conversion_to_usd.get(currency)
    if rate:
        usd_amount=bill_amount*rate
    else:
        logger.info(f"no rate found for currancy {currency}")
    
    print(f" id : {id}, currency : {currency}, rate : {rate}.")
def lambda_handler(event, context):
    try:
        bucket_name=event['Records'][0]['s3']['bucket']['name']
        s3_file=event['Records'][0]['s3']['object']['key']
    
        response=s3_client.get_object(Bucket=bucket_name, Key=s3_file)
        data=response['Body'].read().decode('utf-8')
        csv_reader=csv.reader(io.StringIO(data))
        next(csv_reader)
    
        for record in csv_reader:
            process_record(record)
        logger.info("Lambda has finished successfully")
        
    except Exception as e:
        logger.error(f"Error : unexpected error {e}")
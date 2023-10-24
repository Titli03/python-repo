import json
import boto3
import logging
from datetime import datetime

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2=boto3.client('ec2')
    current_date=datetime.now().strftime("%y-%m-%d")
    
    try:
        response=ec2.create_snapshot(
            VolumeId='vol-0c94c63f1597cf43d',
            Description='my ec2 snapshot',
            TagSpecifications=[
                {
                    
                     'ResourceType':'snapshot',
                     'Tags': [
                         {
                             'Key':'Name',
                             'Value':f"my ec2 snapshot {current_date}"
                             }
                         ]
                     }
                
                ]
            
            
            
            )
        logger.info(f"successfully created snapshot {json.dumps(response, default=str)}")
    except Exception as e:
        logger.error(f"error creating snapshot {str(e)}")
   

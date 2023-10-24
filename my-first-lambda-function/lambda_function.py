import json

def lambda_handler(event, context):
    # hellow from cloud9
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

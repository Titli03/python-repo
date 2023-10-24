def main():
    user_requirement='serverless_computing'
    
    if user_requirement == 'file_storage':
       aws_service='3'
    elif user_requirement == 'virtual_server':
        aws_service='ec2'
    elif user_requirement == 'serverless_computing':
        aws_service='Lambda'
        
    else:
      aws_service='unknown'  
    
    
    if aws_service !='Lambda':
       print(f'Error ! aws sercive is  {aws_service}') 
    else:
       print(f'aws sercive is reqiued as {aws_service}')






if __name__ == '__main__':
    main()
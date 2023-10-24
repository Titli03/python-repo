def main():
    aws_service=['s3','lambda','ec2','dynamodb']
    #print(f'aws_serviceslist = {aws_service}')
    #print(aws_service[0])
    last_item = aws_service[-1]
    aws_service[-1]='sqs'
    #print(last_item)
    aws_service.append('sns')
    #print(f'aws_serviceslist = {aws_service}')
    aws_service.pop(1)
    print(f'aws_serviceslist = {aws_service}')
    sliced_item = aws_service[1:2]
    print(f'sliced_item = {sliced_item}')
    list_lengthe= len(aws_service)
    print(f'length of aws_service lis is {list_lengthe}')
    
    
    
    
    
    
    
    
    
    
    
    




if __name__ == '__main__':
    main()
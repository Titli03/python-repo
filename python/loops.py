def main():
    aws_service = ['ec2','lambda','s3','sns']
    #print(aws_service)
     #for status in aws_service:
         #print(f'the status is {status}')
        
    index = len(aws_service)-1
    while index >0:
        #print(aws_service[index])
        index-=1
    for index, status in enumerate(aws_service):
        print (f'{index+1} : {status}')
    
        
        
     








if __name__ == '__main__':
    main()
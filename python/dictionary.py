def main():
  aws_service={
    's3':'simple storage service',
    'lambda':'serverless',
    'ec2':'compute system'
  }  
  

  aws_service['lambda'] = 'serverless service'
  lambda_description = aws_service['lambda']
  print(lambda_description)
  aws_service['sns'] = 'simple msg service'
  #aws_service['lambda'] = 'serverless service'
  #print(f"sns: {aws_service['sns']}")
  #del aws_service['lambda']
  #print(f'{aws_service}')
  #print(aws_service.keys())
  #print(aws_service.values())
  #print(aws_service.items())
  
  aws_service['ec2'] = {
    'description':'elastict compute center',
    'year':'2023'
  }
  
  print(f'{aws_service}')
   
  
  
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
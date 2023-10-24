def main():
   service='gufran' 
   service_status=get_service(service)
   if service_status:
      print(f"{service} service status : '{service_status}'")
   
      if service_status == 'operational':
          print(f"'{service}' is operational")
      else:
          print(f"'{service}'is not operational")
   else:
        print(f"{service} service status can not be retrieve")
        
def get_service(service_name):
    aws_service_name ={
        'ec2':'compute',
        'lambda':'serverless',
        'rds':'operational'
        
    }
    try:
        return aws_service_name[service_name]
    except KeyError as ke:
        print(f"Error : {ke} status for aws service {service_name} is not available in our recod ")
        return None
      
    
    
    
if __name__ == '__main__':
    main()
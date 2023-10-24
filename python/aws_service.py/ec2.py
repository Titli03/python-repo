import boto3
ec2=boto3.resource('ec2')
instance_name='my ec2 via python'
instance_id= None
instances=ec2.instances.all()
instance_exists=False
for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists=True
            instance_id=instance.id
            print(f"{instance_name} is already present with {instance_id}")
            break
    if instance_exists:
        break
if not instance_exists:

    new_instance= ec2.create_instances(
           ImageId= 'ami-0df435f331839b2d6',
           MinCount=1,
           MaxCount=1,
           InstanceType='t2.micro',
           KeyName='my_key_pair',
           TagSpecifications=[
               {
                   'ResourceType': 'instance',
                   'Tags': [
                       {
                           'Key':'Name',
                           'Value': instance_name
                       },
                    ] 
               },
            ]
    
    )
    instance_id = new_instance[0].id
    print(f"{instance_name} is creted with id : {instance_id}")
#ec2.Instance(instance_id).stop()
#print(f"{instance_name} with id: {instance_id} is stopped now")
#ec2.Instance(instance_id).start()
#print(f"{instance_name} with id: {instance_id} is started now")
ec2.Instance(instance_id).terminate()
print(f"{instance_name} with id: {instance_id} is terminated now")
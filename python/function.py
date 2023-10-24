def main():
    meterials_1 = ["leather","rubber"]
    meterials_2 = ["gargage","new"]
    meterials_3 = ["mess","rubber"]
    shoe_1 = create_shoe(meterials_1)
    shoe_2 = create_shoe(meterials_2)
    shoe_3 = create_shoe(meterials_3)
    
    shoes = [shoe_1,shoe_2,shoe_3]
    for shoe in shoes:
         if shoe['type'] == 'unknown':
             print(f"unknown shoe type : {shoe['meterials']}")
         else:
            print(f"shoe_type is : {shoe['type']}") 
    
     #print(f"shoe_type is : {shoe_1['type']}")
     #print(f"shoe_type is : {shoe_2['type']}")
     #print(f"shoe_type is : {shoe_3['type']}")
    
def create_shoe(meterials_list):
    shoe_type=''
    if 'leather' in meterials_list and 'rubber' in meterials_list:
        shoe_type = 'boot'
    elif 'mess' in meterials_list and 'rubber' in meterials_list:
        shoe_type = 'sniker'
    else:
        shoe_type = 'unknown'
    
    
    
    return {'type': shoe_type, 'meterials' : meterials_list}
       
    
    
    
    
    







if __name__ == '__main__':
    main()
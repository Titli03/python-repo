def main():
    
    item_name='banana'
    quantity=5
    discount_rate=0.1
    elegible_item="orange banana carrot"
    item_price=2
    
    subtotal=item_price*quantity
    
    #print(f"item_name: {item_name} subtotal is {subtotal}")
    
    if item_name in elegible_item:
       discount=discount_rate*subtotal
    #print(f"discount is : {discount}")   
    
    was_discount_applied=discount>0
    
    #print(f"was_discount_applied? {was_discount_applied}")
    
    does_free_shipping_applied=quantity>=5 and item_name == 'banana'
    print(f"if the item is eligible for free shipping? {does_free_shipping_applied}")
    
    
    












if __name__ == '__main__':
    main()
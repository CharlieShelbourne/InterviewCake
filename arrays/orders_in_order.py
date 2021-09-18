
# Not first come first served: 

# take out [1, 3, 5]
# dine in = [2, 4, 6]

# served orders = [1, 2, 4, 6, 5, 3]

# 3 served before 5 

# first come first served: 

# take out [17, 8, 24]
# dine in [12, 19, 2]

# served orders = [17, 8, 12, 19, 24, 2]

# take out [1, 3, 5]
# dine in = [2, 4, 6]

# served orders = [1, 2, 4, 6, 5, 3]

# order number arbitary only position matters 

def is_service_first_come_fist_served(served_orders: list, take_out: list, dine_in: list) -> bool:
    # loop through served orders (tracking) and check if out of place orders
    take_out_ind = 0
    dine_in_ind = 0
    for order in served_orders:
        if take_out_ind < len(take_out) and order == take_out[take_out_ind]:
            take_out_ind += 1
        elif dine_in_ind < len(dine_in) and order == dine_in[dine_in_ind]:
            dine_in_ind += 1
        else: 
            return False 
    return True

take_out = [17, 8, 24]
dine_in = [12, 19, 2]

served_orders = [17, 8, 12, 19, 24, 2] 

take_out =  [1, 3, 5]
dine_in = [2, 4, 6]

served_orders = [1, 2, 4, 6, 5, 3]
    
print(is_service_first_come_fist_served(served_orders, take_out, dine_in))


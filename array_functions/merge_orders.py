# each order a unique integer 
# 2 lists one dine in one dine out
# orders should be sequential
# no limit on distance between order numbers 
# if next order in list is lower than the previoud the sequence starts again 


# cannot merg the list then order them 
# track poistion in lists and use out of place function to generate new list 

# functions
# use helper function to create ordered list for per sequence
# requires sequence star and end to be tracked 
# function to detect sequences, use to detect starting positions

# inputs: 
# [17, 8, 24]
# [12, 19, 2]

# output: 
# [17, 8, 12, 19, 24, 2]

def append_inside(inside: list, outside: list, inside_ind: int, outside_ind: int) -> bool:
    if len(inside) < 1:
        return False
    if len(outside) < 1:
        return True

# start if value is greater than oposite and next val 
    # check if outside list finished
    if outside_ind >= len(outside) or ( 
        # when inside list is before its last order check it should be placed before the current order on outside list and its the end of a sequence
        inside_ind < (len(inside)-1) and inside[inside_ind] > outside[outside_ind] and inside[inside_ind] > inside[inside_ind+1]) or (
        # when inside list is on its last order but outside list is not check for start of new sequence
        inside_ind == len(inside)-1 and outside_ind > 0 and outside[outside_ind] < outside[outside_ind-1]
        ):
        
        return True
    elif inside_ind >= len(inside) or ( 
        # when outside list is before its last order check it should be placed before the current order on inside list and its the end of a sequence
        outside_ind < (len(outside)-1) and outside[outside_ind] > inside[inside_ind] and outside[outside_ind] > outside[outside_ind+1]) or (
        # when outside list is on its last order but inside list is not check for start of new sequence
        outside_ind == len(outside)-1 and inside_ind > 0 and inside[inside_ind] < inside[inside_ind-1]
        ):
        return False
    # if not begining or end of a sequence place the smaller value first 
    elif inside[inside_ind] < outside[outside_ind]:
        return True
    else:
        return False 

def merge_orders(inside: list, outside: list) -> list: 
    if len(inside) + len(outside) < 1:
        return []

    inside_ind = 0
    outside_ind = 0
    merged_lists = []
    while len(merged_lists) < len(inside) + len(outside):
        if append_inside(inside, outside, inside_ind, outside_ind): 
            merged_lists.append(inside[inside_ind])
            inside_ind += 1
        else:
            merged_lists.append(outside[outside_ind])
            outside_ind += 1
    return merged_lists
        

# inputs: 
inside = [17, 8, 24]
outside =  [12, 19, 2]

# next number is less than current 

print(merge_orders(inside, outside))

# output: 
# [17, 8, 12, 19, 24, 2]


'''
constraints:
each list is alreadysorted in order 
merges list must be in numberical order 

edge cases: 
[1,2,3], [4,5,6] 
[4,5,6], [1,2,3] 
[1,4,7], [3,5,9] 
[3,5,9], [1,4,7]

'''

def merge_sorted(sorted_a: list, sorted_b: list): 
    a_ind = 0
    b_ind = 0 
    sorted_list = []
    while len(sorted_list) < len(sorted_a) + len(sorted_b):
        if a_ind < len(sorted_a) and (b_ind >= len(sorted_b) or sorted_a[a_ind] < sorted_b[b_ind]): # Short circuit evaluation because b_ind >= len(sorted_b) python does not check sorted_a[a_ind] < sorted_b[b_ind]
            sorted_list.append(sorted_a[a_ind])
            a_ind += 1
        else:
            sorted_list.append(sorted_b[b_ind])
            b_ind += 1
    return sorted_list


my_list     = []
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_sorted(alices_list, my_list))





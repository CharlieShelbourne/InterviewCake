def merge_sort(ranges: list) -> list: # inplace function
    if len(ranges) < 2:
        return ranges

    mid_index = int(len(ranges)/2)
    left = ranges[:mid_index]
    right = ranges[mid_index:]

    sorted_left = merge_ranges(left)
    sorted_right = merge_ranges(right)

    sorted_ranges = []
    current_ind_left = 0
    current_ind_right = 0
    
    while len(sorted_ranges) < len(left) + len(right):
        if (current_ind_left < len(left)) and (current_ind_right == len(right) or sorted_left[current_ind_left][0] < sorted_right[current_ind_right][0]):
            sorted_ranges.append(sorted_left[current_ind_left])
            current_ind_left += 1
        else:
            sorted_ranges.append(sorted_right[current_ind_right])
            current_ind_right += 1
    
    return sorted_ranges


def merge_ranges(ranges: list) -> list:
    if len(ranges) < 2:
        return ranges
    sorted_ranges = merge_sort(ranges)
    sorted_ranges = ranges
    limit = len(sorted_ranges)-1
    i = 0
    while i < limit:
        if sorted_ranges[i][1] > sorted_ranges[i+1][0]:
            if sorted_ranges[i][1] > sorted_ranges[i+1][1]: # makes changes inplace
                sorted_ranges.pop(i+1)
                i=-1
            else:
                sorted_ranges[i] = (sorted_ranges[i][0], sorted_ranges[i+1][1])
                sorted_ranges.pop(i+1)
                i=-1
            limit = limit - 1
        i += 1
    return sorted_ranges


ranges =  [(1, 10), (2, 6), (3, 5), (7, 9)]
ranges = merge_ranges(ranges)
print(ranges)

def pivot_index(arr:list)->int:
    sum_arr = sum(arr)
    for index in range(len(arr)):
        current_sum = sum(arr[0:index])
        if current_sum == sum_arr - current_sum - arr[index]:
            return index
    return -1
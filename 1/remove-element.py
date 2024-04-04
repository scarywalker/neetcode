def remove_element(nums:list,val:int)->list:
    for index in range(len(nums)-1,-1,-1):
        if nums[index] == val:
            nums.pop(index)
    return nums
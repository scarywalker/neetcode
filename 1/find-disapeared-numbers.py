def find_disapeared_number(nums:list)->list:
    output:list = []
    for index in range(len(nums)):
        if index + 1 not in nums:
            output.append(index+1)
    return(output)
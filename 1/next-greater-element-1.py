def next_greater_element(nums1:list,nums2:list)->list:
    ans:list = []
    for i in nums1:
        resolved:bool = False
        for j in nums2[nums2.index(i) + 1:]:
            if j > i:
                ans.append(j)
                resolved = True
                break
        if not resolved:
            ans.append(-1)
    return ans
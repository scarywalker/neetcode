def contains_duplicate(arr):
    for element in arr:
        if arr.count(element) > 1: return True
    return False
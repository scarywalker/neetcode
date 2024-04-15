def find_index_first(haystack:str,needle:str):
    for index in range(len(haystack)):
        if needle == haystack[index:index+len(needle)]:
            return index 
    return -1

def is_subsequence(string1,string2):
    i,j = 0,0
    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]: i += 1
        j += 1
    return i == len(string1)
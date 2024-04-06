def isomorphic_string(string1:str,string2:str):
    temp:dict = {}
    for index in range(len(string1)):
        if (string1[index] not in temp):
            temp[string1[index]] = string2[index]
        if temp[string1[index]] != string2[index]:
            return False
    return True


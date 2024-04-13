def word_split(pattern:str,text:str)->bool:
    temp:dict = {}
    text_list = text.split()
    if len(pattern) != len(text_list):
        return False
    for index in range(len(pattern)):
        if pattern[index] not in temp:
            temp[pattern[index]] = text_list[index]
        if temp[pattern[index]] != text_list[index]:
            return False
    return True
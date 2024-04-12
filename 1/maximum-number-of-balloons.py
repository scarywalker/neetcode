def maximum_number_of_balloons(text:str)->int:
    temp:list = []
    for char in "balon":
        count = text.count(char)
        if char == "l" or char == "o":
            count = count/2
        temp.append(count)
    return sorted(temp)[0]
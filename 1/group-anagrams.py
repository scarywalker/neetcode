def group_anagrams(word_list:list)->list:
    output:list = []
    while len(word_list) > 0:
        current_word:str = word_list.pop()
        if len(output) < 1:
            output.append([current_word])
        else:
            is_there:bool = False
            for element in output:
                if sorted(element[0]) == sorted(current_word):
                    element.append(current_word)
                    is_there = True
            if not is_there:
                output.append([current_word])
    return output
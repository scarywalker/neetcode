def length_of_last_word(sentence:str)->int:
    last_word = sentence.split(" ")[-1]
    return len(last_word)
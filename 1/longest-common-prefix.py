def longest_common_prefix(word_list:list)->str:
    output = ""
    for i in range(len(word_list[0])):
        char = word_list[0][i]
        for word in word_list:
            if len(word) == i or word[i] != char:
                return output
        output += char
    return output

print(longest_common_prefix(["flowergdsgdgs","f","flight"]))
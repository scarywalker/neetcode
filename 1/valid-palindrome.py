def valid_palindrome(input:str)->bool:
    input = input.lower()
    alnum = ""
    for char in input:
        if char.isalnum():
            alnum += char
    return alnum == alnum[::-1]
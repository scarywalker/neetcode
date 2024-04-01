def valid_anagram(word1,word2):
    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False
    return True
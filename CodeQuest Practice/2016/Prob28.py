import string

def is_anagram(str1, str2):
    # remove spaces and punctuation from both strings
    str1 = str1.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    str2 = str2.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    
    # sort both strings alphabetically
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # compare sorted strings
    return sorted_str1 == sorted_str2


cases = int(input())

for caseNum in range(cases):
    word_1, word_2 = input().split("|")
    if word_1 == word_2:
        result = "NOT AN ANAGRAM"
    elif is_anagram(word_1, word_2):
        result = "ANAGRAM"
    else:
        result = "NOT AN ANAGRAM"
    print(f"{word_1}|{word_2} = {result}")

    # Solved
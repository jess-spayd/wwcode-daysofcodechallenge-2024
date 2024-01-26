# Write a function that counts the frequency of each word in a sentence.
from collections import defaultdict

def count_words(sentence: str):

    word_list = sentence.split(" ")
    word_count = defaultdict(int)

    for word in word_list:
        word_count[word] += 1
    
    return word_count

user_input = input("Type a sentence: ")

print(count_words(user_input))


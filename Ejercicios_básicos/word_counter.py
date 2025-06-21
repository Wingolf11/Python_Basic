#Exercise: Word Counter
#Write a Python program that:

#1. Asks the user to input a sentence.
#2. Counts the number of words in the sentence.
#3. Prints the word count to the user.

def check_for_char(word_list):
    total = 0
    for word in word_list:
        for char in word:
            if char == "'":
                total += 1
    return  total

Sentence = input("Enter a sentence: ")
word_list = list(map(str, Sentence.split(" ")))
word_count = len(word_list) + check_for_char(word_list)
print("The word count is: " + str(word_count))

#-> take in count words with: '
#this word is multiplied by 2
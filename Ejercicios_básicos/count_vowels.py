sentence = input("Enter a string or sentence: ")
vowels = ['a','e','i','o','u']
count_vowels = 0

for letter in sentence:
    for vowel in vowels:
        if letter == vowel:
            count_vowels += 1
print("The number of vowels is: " + str(count_vowels))

    
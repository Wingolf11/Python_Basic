#Exercise: Sum of List Numbers
#Write a Python program that:

#1. Asks the user to input a list of numbers separated by commas (e.g., 1,2,3,4,5).
#2. Converts the input into a list of integers.
#3. Calculates and prints the sum of all the numbers in the list.

def calculate_sum(int_numbers):
    total = 0
    for number in int_numbers:
        total += number
    return(total)

def error_handling(str_numbers):
    for letter in str_numbers:
        if not (letter.isdigit() or letter == ','):
            print("Input Error: numbers are not valid!")
            break

str_numbers = input("Enter numbers: ")
error_handling(str_numbers)
    
int_numbers = list(map(int, str_numbers.split(",")))

result = calculate_sum(int_numbers)
print("The list is: " + str(int_numbers))
print("Result is: " + str(result))


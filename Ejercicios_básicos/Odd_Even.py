#Exercise: Odd or Even Number Checker
#Write a Python program that:

#1. Asks the user to input a number.
#2. Checks if the number is odd or even.
#3. Prints a message to inform the user whether the number is odd or even.

#Bonus:
#Add a feature where the program runs continuously, asking for more numbers until the user types "exit" to stop the program.

import math

def result(number):
    result = int(number) % 2
    if result == 0:
        print("even")
    else:
        print("Odd")


number = 0
while number != "exit":
    number = input("Enter number: ")
    if number == "exit":
        break
    else:
        result(number)
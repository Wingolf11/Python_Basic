
number = input("Enter a number: ")
counter = 2
result = 1
try:
    while   counter <= int(number):
        result = result * counter
        counter += 1
    print("The factorial of " + str(number) + " is " + str(result))
except ValueError:
    print("Please enter a number")
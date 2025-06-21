import math

def result(int_number, i):
    return  (int_number * i)

i = 0
try: 
    str_number = input("Enter a number: ")
    int_number = int(str_number)
    while   i <= 10:
        print(str_number + " x " + str(i) + " = " + str(result(int_number, i)))
        i += 1
except ValueError:
    print("Please enter a valid number.")

def result(number):
    int_number = int(number)
    if  int_number > 0:
        print("number is positive")
    elif    int_number < 0:
        print("number is negative")
    else:
        print("number is equal to zero")


number = 0
while number != "exit":
    number = input("Enter number: ")
    if number == "exit":
        break
    else:
        result(number)
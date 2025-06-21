try:
    numbers = input("Enter numbers: ")
    int_numbers = list(map(int, numbers.split(" ")))
    result = list(map(lambda x: x ** 2, int_numbers))
    print(result)
except ValueError:
    print("Enter valid numbers. For example: 1 5 10 20 5, etc...")
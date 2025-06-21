def fizz_buzz(int_content):
    result = []
    for number in int_content:
        if  number % 5 == 0 and number % 3 == 0:
            result.append("FizzBuzz")
        if  number % 5 == 0:
            result.append("Buzz")
        elif    number % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(number))
    return  result

with open("source.txt", "r") as file:
    content = file.read()
try:
    int_content = list(map(int, content.splitlines()))
    fb_content = fizz_buzz(int_content)
    print(fb_content)
except  ValueError:
    print("Enter numbers only")
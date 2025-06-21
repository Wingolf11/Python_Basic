def countdown(n):
    while n > 0:
        yield n     #keyword yield very important. allows the countdown
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)

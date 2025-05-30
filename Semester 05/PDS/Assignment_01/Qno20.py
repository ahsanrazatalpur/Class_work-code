number = 12345
min = 10

while number > 0:
    digit = number % 10
    if digit < min:
        min = digit
    number //=10
print(min)
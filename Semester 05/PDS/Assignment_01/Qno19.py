number = 13487
digit = 0
max = 0

while number > 0:
    digit = number % 10
    if digit > max:
     max = digit
    number//=10
print(max)
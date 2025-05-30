number = 1234
digit = 0
even = 0
odd = 0

while(number > 0):
    digit = number % 10
    if(digit %2 == 0):
        even+=digit
    else:
        odd+=digit
    number //=10
print('Sum of even' ,even)
print('Sum of odd' ,odd)
number = 123455
digit = 0
even = 0
odd = 0
difference = 0

while(number > 0):
    digit = number%10
    if(digit %2 == 0):
        even+=digit
    else:
        odd+=digit
    number //=10
    difference = even - odd
print('The difference of Even and Odd is', difference)
print(even)
print(odd)
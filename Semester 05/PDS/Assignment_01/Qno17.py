number = 153
digit = 0
sum = 0
temp = number
length = len(str(number))

while temp > 0:
    digit  = temp % 10
    sum += digit ** length
    temp //=10
if number == sum:
    print('Number is Arsmtromng')
else:
    print('Number is not armstrong') 
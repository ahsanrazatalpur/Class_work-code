# number = 10
# mystr = ""

# while number > 0:
#     base = number % 2
#     mystr = str(base) + mystr
#     number = number//2
# print(mystr)


number = 153
temp = number
sum = 0
length = len(str(number))

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //=10
if number == sum:
    print('number is armstrong')
else:
    print('not armstrong')

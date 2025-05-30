number = 123
digit = 0
product = 1

while(number > 0):
    digit = number % 10
    product = product *digit
    number//=10
print(product)

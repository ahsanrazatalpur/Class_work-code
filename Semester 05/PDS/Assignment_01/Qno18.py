number = 10
rem = 0
my_str = ""

while number > 0:
    rem = number%2
    my_str = str(rem) + my_str
    number= number// 2
print(my_str)
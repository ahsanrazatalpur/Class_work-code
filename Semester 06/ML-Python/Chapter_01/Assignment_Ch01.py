# Chapter 01 Assignment Solve

# Qno 1 Program to Sum two numbers

# a = 10
# b = 40
# result = a + b
# print("Sum :",result)


# Qno 2 Program to Subtract two numbers

# a = 60
# b = 50
# result = a  - b
# print("Subtract :",result)


# Qno 3 Program to Multiply two numbers

# a = 10
# b = 5
# result = a * 5
# print("Multiplication :",result)


# Qno 4 Program to Divide two numbers

# a = 10
# b = 2
# result = a / b
# print("Division : ",result)


# Qno 5 Program to Remainder two numbers

# a = 100
# b = 20
# result = a % b
# print("Reminder :",result)


# Qno 6 Program to Remainder two numbers
# number1 = int(input("Enter 1st integer : "))
# number2 = int(input("Enter 2nd integer : "))

# print("Addition       :",number1 + number2)
# print("Subtraction    :",number1 - number2)
# print("Multiplication :",number1 * number2)
# print("Division       :",number1 / number2)
# print("Modulus        :",number1 % number2)


# Qno 7 Program to find average of three numbers

# number1 = int(input("Enter 1st number : "))
# number2 = int(input("Enter 2nd number : "))
# number3 = int(input("Enter 3rd number : "))

# print((number1 + number2 + number3)/3)


# Qno 8 Program to find area of rectangle 

# width = float(input("Enter the width of rectangle   : "))
# length = float(input("Enter the length of rectangle : "))
# print("The are of Rectangle is : " , width * length)


# Qno 9 Program to find perimeter of square

# perimeter = float(input("Enter the perimeter :"))
# print("Perimeter :" ,4 * perimeter)


# Qno 10 Program to covert cel into farhenheit temperature

# cal = float(input("Enter temperature in Calcuis :"))
# print("Temperature in Farhenheit is :", (cal * 9/5) + 32)


# Qno11  Program to count number of digit 

# number = int(input("Enter your number : "))
number = 576
count = 0
while number > 0:
 digit = number % 10
 count = count + 1
 number = number / 10

print(count)
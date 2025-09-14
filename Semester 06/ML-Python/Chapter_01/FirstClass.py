# # Repeat of last 5th semseter

# # output

# # These are the common output of python

# a = "Machine Learning"
# b = 100
# c = 10.8 
# d = False
# d = None 

# print(a)
# print(b)
# print(c)
# print(d)


# # type() function to print the type of that datatype
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# # len() function to print the length of datatype
# print(len(a))
# # print(len(b)) # type error  int , float , Nonetype has no length
# # print(len(c)) # type error
# # print(len(d)) # type error


# # round() function to round off the value
# # remeber rule : 
#     # 1.   value greater than .5 will be extend to upper value
#     #      eg : 10.6 , 10.7 , 10.8 , 10.9 will be 11
#     # 2.   value less than .5 will be decrease to lower value
#     #      eg : 10.1, 10.2, 10.3, 10.4 will be 10
#     # 3.   value .5 also decrease to lower number 
#     #      eg : 10.5 will be 10

# num = 10.6
# num2 = 20.2
# num3 = 50.5

# print(round(num))
# print(round(num2))
# print(round(num3))



# # max() and min() to find max and min value 
# print(max([10, 20, 30])) #30
# print(min([10, 20, 30])) #10

# # sum() to add / sum value
# print(sum([10, 20, 30])) #60

# # sorted() sort the value
# print(sorted([10, 30, 20]))


# question take string an input and print each alphabet through for in loop
# name = input("Please enter your name? ")
# for i in name:
#     print(i)

# for i in len(name):
#     print(i[name])



# way to print string
# name = 'Ahsan raza'  # string can be in single quote
# name2 = "Ali Raza"   # string can be in doublr quote
# name3 = """Mehdi Raza is a good boy,
# he is my nephew,
# he will be doctor""" # string can be in triple quote

# print(name)
# print(name2)
# print(name3)



# escape sequence
# 1. \n for new line
# 2. \t for tab space
# 3. \\
# 4/ \" "\ double quote
# 5. '' single quote
# 6. \r carriage return (move cursor to start of line)
# 7. \b delete one character
# 8. \u for unicode character
#9. \r to donot treat python as escape sequence


# \n 
# print("My name is Ahsan raza\nMy age is 21\nI live in badin")
# #\t 
# print("I love my country\tI would love to sacrifice my lifi to my country")
# # \\
# print("If youn has to choose superpowe which one you choose Flying\\Disapearing")
# #\" "\
# print("The full name of pakistan is \" Islami Jamhoria Pakistan\" .")
# # \r
# print("we are using carraig \rfor return the cursor to start")
# #\b 
# print("Hello Worldd\b")
# # \u 
# # print("We are testing random unicode \u2764")
# # \r
# print("\r C:\Users\PMYLS\Desktop\Ahsan\Sixth Semester\ML-Python\FirstClass.py, line 68, in <module>")


# str = "Pakistan Zindaabad"
# print(str)
# print(type(str))
# print(len(str))
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])
# print(str[5])

# String formating
# str[start : end : step]
# print(str[:]) #Pakistan
# print(str[:6]) # it will run until 6 character 
# print(str[::2]) 
# print(str[3:7:3]) 

# start mean start position always 0
# end mean end position always start from 1 to n
# step mean jump 

# str = 'Pakistan'----------------------------------
# print(str[-1:8:2])


# string formating old way
# print("My name is {} and my age is {} and I live in {}".format("Ahsan",20,"badin"))
# print("My name is {} and My age is {} and I live in {}".format(20,"Badin","Ahsan"))
# print("My name is {2} and My age is {0} and I live in {1}".format(20, "Badin", "Ahsan"))

# name = "Ahsan"
# age = 20
# country = "Pakistan"
# print("My name is {} and My age is {} and My country is {}".format(name , age , country))
# print("My name is {name} and My age is {age} and I live in {city}".format(name = "Ahsna" ,age = 20, city = 'Badin'))

# # new Formating way
# print(f"My name is {name} and my age is {age}")

# once tens hundred

# number = int(input("Enter any number between 999 to 9999 : "))
# # number is 5555
# once = number % 10
# tens = (number // 10 ) %10
# hundred = (number // 100 ) %10
# thousand = (number // 1000 ) %10

# print("Once :",once)
# print("Tens :",tens)
# print("Hundred :",hundred)
# print("Thousand :",thousand)


# number = int(input("Enter any number from 999 to 9999 :"))

# once = number % 10
# tens = (number // 10) %10
# hundred = (number // 100) %10
# thousand = (number // 1000) % 10

# print("Once :", once)
# print("Tens :", tens)
# print("Hundred :", hundred)
# print("Thousand :", thousand)



# arithamatic operator

# + Addition
# - Substraction
# * multiplication
# / Division 
# // Floor division (ignore value after decimal point)
# ** power 
# % modulus (remainder)

# print( 20 + 30)
# print( 20 - 30)
# print( 20 * 30)
# print( 20 / 30)
# print( 20 % 30)
# print( 20 ** 30)
# print( 20 // 30)

# Additional operator (Augmented assignment operator)

# +=
# -=
# *=
# /=
# %=
# //=
# **=

# 10 + 28 # This called error because 10+28 = 38 then what we do with 38 
# x = 10
# x += 28
# print(x)

# x = 10
# x -= 28
# print(x)

# x = 10
# x *= 28
# print(x)

# x = 10
# x %= 28
# print(x)

# x = 10
# x /= 28
# print(x)

# x = 10
# x //= 28
# print(x)

# x = 10
# x **= 28
# print(x)


# input in Python
# # string input
# name = input("Enter any name :")
# print("Your name is : " , name)

# # number input
# number = int(input("Enter any number  :"))
# print("Your Enterd number is :",number)


# PI = 3.142
# print(PI)
# PI = 3.1734
# print(PI)

# a,b,c,d = 10,20,30,40
# print(a)
# print(b)
# print(c)
# print(d)


# a,b,*c= 10,20,30,40,50
# print(a)
# print(b)
# print(c)

# bin,drc conersion
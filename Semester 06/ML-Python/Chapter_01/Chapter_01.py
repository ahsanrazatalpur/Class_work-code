
# print("Hello")  #Printing  Normal string 
# print(10)  #Printing  Integer
# print(100.0) #Printing  float (decimal value by default float in python)
# print(None) #Printing  None value (represents "no value" or "null" in Python)
# print(True) #Printing  Boolean value (True or False)
# print(" ") #Printing  space  (just an empty space character)



# Arithamatic operation

# print(90 + 10)   # + for addition
# print(110 - 10)  # - for subtraction (right number from left)
# print(10 * 10)   # * for multiplication
# print(10 % 10)   # % for modulues (remainder of division)
# print(10 / 10)   # / for division
# print(2 ** 5)    # ** for Exponential power (to give power to left value eg 2 ** 3 mean 2 * 2 * 2 = 8 ) 

# print(30 // 60)  # // for floor division (cut out or ignore value after decimal point eg 10.5 will be 10)
# here is twist in floor division
# if value is positive  eg:  7 // 5 then  the normal division is 1.4 but the floor divison will be rounds down 1
# if value is negative  eg:  -7 // 5 then  the normal division is -1.4 but the floor divison will be rounds down -2 (nearest smaller)

# built in function 

# 1. type (tell us the type of datatype)

# print(type("Python"))  # <class 'str'>
# print(type(100))   # <class 'int'>
# print(type(10.8))  # <class 'float'>
# print(type(True))  # <class 'bool'>
# print(type(None))  # <class 'NoneType'>
# print(type(""))    # <class 'str'>
# print(type("200")) # <class 'str'>



# printing datatype and their type

# x = "I Love Python"
# print(x) #I Love Python
# print(type(x)) #<class 'str'>

# x = 100
# print(x) #100 
# print(type(x)) #<class 'int'>

# x = 109.3
# print(x) #109.3
# print(type(x)) #<class 'float'>

# x = None
# print(x) #None
# print(type(x)) #<class 'NoneType'>

# x = True
# print(x) #True
# print(type(x)) #<class 'bool'>

# x = "190"
# print(x) #190
# print(type(x)) #<class 'str'>

# x = 0
# print(x) #0
# print(type(x)) #<class 'int'>



# Type promotion (mean the automatic conversion of datatype from smaller less general to larger more general so data can't lose)

# x = 20 + 30.7 # int + float
# print(x) # 50.7
# print(type(x)) # <class 'float'>



# 2. round()

# print(round(10))   #10
# print(round(10.4)) #10
# print(round(10.5)) #10
# print(round(10.6)) #11
# print(round(0))    #0

# rules of round fuction
 # 1. If  value after decimal point is less than 5 then value goes backward  eg -> 10.4 will be 10 only
 # 1. If  value after decimal point is equal to 5 then value goes nearest even number  eg -> 10.5 will be 10  and 11.5 will be 12
 # 1. If  value after decimal point is greater than 5 then value goes upward  eg -> 10.6 will be 11 



# 3. abs() built in function to return absolute value (remove any sign + or -)

# print(abs(10))
# print(abs(-110))
# print(abs(0))



# # 4. bin() to convert an integer to binary number
# print(bin(10))   #0b1010
# print(bin(0))    #0b0
# print(bin(100))  #0b1100100
# print(bin(1000)) #0b1111101000
# print(bin(-10))  #-0b1010


# 5. int() to convert any datatype to integer

# print(int(0b0))       #0
# print(int(0b1010))    #10
# print(int(0b1100100)) #100

# # int can take also string with base 
# print(int('0', 2))        #0
# print(int('1010', 2))    #10
# print(int('1100100', 2))   #100


# print(type('hello World !'))  #<class 'str'>
# print(type('The student Of Computer Science')) #<class 'str'>

# my_str = "My name is Ahsan Raza\nI Live in Badin\nI study in Computer Science"  #\n escape sequence for new line
# print(my_str)

# my_str = """The Vice Chansolr       
#                         Laar Campus badin
#      Dated : 2 Sep 2025"""
# print(my_str) # Triple quote print as it is


#  Define a constant value for PI
# PI = 3.142
# print(PI)
# print(type(PI))  #<class 'float'>

#  Multiple variable assignment in one line
# a,b,c = 10,20,30
# print(a) #10
# print(b) #20
# print(c) #30

# Extended unpacking: a and b take the first two values, 
# remaining values go into a list 'c'
# a,b,*c = 10,20,30,40,50
# print(a) #10
# print(b) #20
# print(c) #[30, 40, 50] -> stored as a list



# x = 10
# x + 5 # In this line we have add 5 to value of x but did't assigned to x  , so x remian unchanged
# # what will be x now ?  x remian same
# print(x) #10

# # add 5 to the value of x and assigned it to x
# x = x + 5
# print(x) #15

# # Shorthand assignment operators (compound assignments)
# x += 5
# print(x) #20
# x -= 5
# print(x) #15
# x *= 5
# print(x) #75
# x /= 5
# print(x) #15.0
# x //= 5
# print(x) #3.0
# x **= 5
# print(x) #243.0
# x %= 5
# print(x) #3.0



# program to find the Onces, Tens , Hundreds, Thousands .. in a given Number

# num = int(input("Enter any number from 999 to 9999 :")) <-- My way

# print("Onces : ",num % 10)
# print("Tens : " ,(num // 10) %10 )
# print("Hundreds : ", (num // 100 ) %10)
# print("Thousands : ",(num // 1000 ) %10)

x = int(input("Enter any number from 999 to 9999 : "))
# x = 8900

y = x / 1000
y = int(y)
print(y)
x= x % 1000 

y = x / 100
y = int(y)
print(y)
x = x % 100

y = x / 10
y = int(y)
print(y)
x = x % 10
print(x)
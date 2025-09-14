# Here is Chapter 02 (Topic 2 solve) repeat of sems 5th

# Concatenate String
# name  = "Ahsan Raza"
# age = 20

# print("My name is ",name , "And My age is 20") concatenate string and number cause error
# print(name+age) #TypeError: can only concatenate str (not "int") to str


# Concatenate String ang Integer by changing their datatype
# number1 = 10    # int
# number2  ="20"  # str
# print(number1 + number2) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(number1 + int(number2)) #Concatenate one Sting and one int by changing one 'str' into 'int'
# print(str(number1) + number2) # Concatenate one string and one integer by change one 'int' into 'String'



# Checking and changing Datatype
# my_str = "I love Python"
# Exp = 2

# print(type(my_str)) # <class 'str'>
# print(type(Exp))    # <class 'int'>
# print(str(Exp))     # 2  (change 'int' into 'str')
# print(type(Exp))    # <class 'int'>




# changing type twice in single line
# print(type(6))                #<class 'int'>
# print(type(str(6)))           #<class 'str'>
# print(type(str(int(6))))      #<class 'str'>
# print(type(str(int(str(6))))) #<class 'str'>


#Escape Sequence
# \n for new line
# \t for tab spaces
# \" \" for double quote
# \b for backspace 
# \r for carraiage return
# \\ For single quote



# \n for new line
#print("My name is Ahsan Raza\nI live in Badin\nI study in Laar campus Badin")

# \t for tab spaces
#print("My name is Ahsan Raza\tI have use Tab space")

# \" \" for double quote
#print("My name is \"Ahsan Raza\" and I live in \"Badin\"")

# For single quote''
#print("My name is Ahsan Raza and My age is'20'")

# \b for backspace 
#print("Helloo\b World!")

# \r for carraiage return
#print("My name is Ahsan Raza Talpur\rand I live in Badin")

# \\ For single quote
# print("Please Select your gender Male\\Female")




# Old way of String Formating

# print("My name is {} and My age is {}".format("Ahsan Raza",20))
# My name is Ahsan Raza and My age is 20

# print("My name is {} and My age is {}".format(20,"Ahsan Raza"))
# My name is 20 and My age is Ahsan Raza

# print("My name is {0} and My age is {1}".format(20,"Ahsan Raza"))
# My name is 20 and My age is Ahsan Raza
# print(age) # Cannot print outside

# print("My name is {name} and My age is {age}".format(name = "Ahsan Raza" , age = 20))


# New way to fomating String

# name = "Ahsan Raza"
# age = 20
# print(f"My name is {name} and My age is {age}")


# String Indexing

# country = "Pakistan"
# print(country)
# print(country[0])
# print(country[2])
# print(country[3])
# print(country[4])
# print(country[5])
# print(country[6])
# print(country[7])

# print(country[3])
# print(country[9])  # out of index



# for in loop
# for i in range(start, end , stepover)

# for i in range(12):  # here always range print as range -1  # 0, 1, 2, ..... 11
#     print(i)

# for i in range(0, 13):  # 0, 1, 2, ..... 12
#     print(i)

# for i in range(1, 13):   # 1, 2, ..... 12
#     print(i)

# for i in range(1, 22, 2):  # 1, 3, 5, .... 21  (Odd numbers)
#     print(i)  

# for i in range(0, 21, 2):   # 0, 2, 4, 6 .. 20 (Even numbers)
#     print(i)



# String built in function len()

# name = "Mehdi Raza"
# print(len(name)) # 10

# selogan = "Pakistan Zndaabad"
# print(len(selogan)) # 17


# name = "Mash Burnended"
# print(len(name))  # 14
# print(type(name)) # <class 'str'>
# for char in name: # M a s h b u r n e n d e d
#     print(char)


# department = "Computer Science"
# for char in department:
#     print(char) # c o m p u t e r s c i e n c e


# String slicing
# print(name[start:end:stepover])

name  = "Ahsan Raza"
print(name)
print(type(name))
print(len(name))

print(name[0:7:]) # Ahsan R
print(name[1:9])  # hsan Raz
print(name[2:8])  # san Ra
print(name[3:6])  # an 
print(name[::-1]) # azaR nashA
print(name[::-2]) # aa ah
print(name[1:8:-1]) # h , a      ------------------------------
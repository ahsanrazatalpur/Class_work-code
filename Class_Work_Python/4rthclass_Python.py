"""
a = True
b = False

print(a) #True
print(b) #false

# pre-bult in function  bool
num = 300
print(bool(num)) #True

str = "Python"
print(bool(str)) #True

space = " "
print(bool(space)) #True

float = 34.56
print(bool(float))

value = None
print(bool(value))

# Type conversion
name = "Ahsan"
print(f"My name is {name}")

# birthday =input("Enter your bithday :")
# print(2025 - birthday) # got error bc string cannot minus from integer
 
birthday =int(input("Enter your bithday :"))
print(2025 - birthday) 


birthday =input("Enter your bithday :")
age = 2025 - int(birthday)
print(age)

# Check Data Type
name = "Ahsan"
phone = 311332
cgpa = 3.5
isStudent = True

print(type(name))
print(type(phone))
print(type(cgpa))
print(type(isStudent))

name = "Mehdi "
print(name * 10)
print(5 * "*")
print(len(name) * "*")

"""
username = input("Enter your username :")
password = input("Enter your password :")

print("Username :",username)
print("Password :",len(password)* '*')

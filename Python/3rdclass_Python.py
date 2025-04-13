# String  Slicing , String is imutable it cannot be changed, once its created 
# string[start :end :stepover]
"""name = "Ahsan Raza"
print(name)
print(name[0])

print(name[1:4:])
print(name)

name[0]='b'
name = 567
print(name)
name = 'Ali'
print(name)
name = "Ahsan Raza"
print(name[:: -1]) # reverse a string using string slicing

#number = 233445  # got error bc string is imutable
#number[0] = 0
#print(number)

# trick to change string index char
name = "Ali raza"
print(name[0:2]+"s"+ name[3:8]) # print string two time once before your change index and print the string you want to and print another slicin by skiping 1 step
 

 # Only the way to reassign the value in string
x = 100  # old string
print(x)
x = 200
print(x) 
name = "Ahsan Raza" # old string
print(name)
name = "Ali raza" # new string
print(name)

# add some value in the strng
num = "1122334" # old string
print(num)
num = "1122334"+"123" # new string
print(num)

name = 'Jake' # old string
print(name)
new_name = name + "john" # new string
print(new_name)

# String Built in function 
greet = 'Heloooooooooog'
print(greet)

# to find length of string
length = len(greet)
print(length)
print(greet[:len(greet)]) # printing whoe string

print[0:14] # Another way to print whole string

 # Pre built-in function i python
name = "salman khan"
print(name)   # printing as it string
print(name.capitalize()) # function to make first letter of word of string capital
print(name.lower())  # function to make first letter of word of string lowercase
print(name.upper()) # function to make string in uppercase
print(name.islower())  # check number is in lowercase
print(name.isupper()) # check number is in uppercase
print(name.find('a')) # find char in string
print(name.find('kh')) # find char in sting
print(name.center) 
print(name.count('a')) # count the givin char in string
print(name.index('k')) # check the index of char in string
print(name.replace('s','p')) # replace one char with another
print(name.split('-')) # spilt string by symbol
print(name.isnumeric()) # check string include number
print(name.isalnum()) # check string is numerical
print(name.isalpha()) # check string is alpha + numerical

  """
#   checking the sentesne is mutable or not
intro = "My name is Ahsan Raza"
print(intro)
newIntro = intro.replace("Ahsan Raza", "Ali Raza") # remember .replace() return a new modified string ,
# it will assign value to new string bc siting is imutable  it doesn't return null as wll
print(newIntro)
print(intro) # it will print ootiginal string 

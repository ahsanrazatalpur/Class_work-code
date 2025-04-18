"""print(bool(0)) # false
print(bool(1)) #true
print('') #false
print(bool("Ahsan")) #true
print(bool(34)) #true

# year =input("Enter your birth year:") 
# age = 2025 - year # got error bc input take in string we have to change it to integer by int function
# print(age)

year = int(input("Please enter your age :")) # here is debug version
age = 2025 - year
print(age)

print("Ahsan"*10) # string multilpy it by 10 (+ and - got error by * and / dont)
print('*'*5)

username = input("Enter your Username :")
password = input("please enter your password :")
hidden =  len(password) * '*'
print("Your username is :",username)
print("Your password is : ", hidden)
# LIST IN PYTHON ( A list is a collection of different type of data in python, It is mutable(changable)) 
li = ['a', 'b', 'c', 'd', 'e', 'f'] # a list of char
print(li)
li2 = [1, 2, 3, 4, 5] # a list of interger
print(li2) 
li3 = [1, 3, 4, "a", "Ahsan", 'e', 34.0] # a list of different type of data
print(li3)

# list slicing in python
cart = ['toy', 'shampoo', 'chicken', 'rings', 'fruit']
print(cart)
print(cart[0]) # accesing single element of list by index
print(cart[4]) 
  
# Note : String is imutable in python

cart = ['toy', 'shampoo', 'chicken', 'rings', 'fruit']
new_cart = (cart[:3])
print(new_cart) 

toys = ['baloon', 'ball', 'doll', 'bat', 'footbal']
new_toy = toys[::-1]
print(new_toy)

names = ['Ahsan', 'Gull', 'Ayaz', 'ALi']
cozns = names
print(cozns) # here we assign one variable value to another that meean refrence is copied to new variables not make new object
# but in case of indexing it assign single by single value so it make new object by string int mn copy banti haii

# NESTED LIST (ARRAY)
matrix = [
    ['Ahsan','Ali','Ayaz','Gull'],
    [20, 25, 29, 24],
    [2.3, 34.3, 4.3, 3.3]
]
print(matrix)
print(matrix[0][0],matrix[2][0])
print(matrix[2][3])
print(matrix[1][3],matrix[0][2])

"""
""" PRE_BUILT FUNCTION IN LIST PYTHON
 1.  .len (to get length of list)
 2.  .append ( to add value (given) at the end of string)
 3.  .insert(insert any value to your choice index)
 4.  .extend (iterable) merge two list)
 5.  .pop() (to remove indexth position value)
 6.  .remove(remove the given value from list)
 7.  .clear (make list empty but dont delte)
 8.  .index (return indexxth value)
 9.  .count(count occurence of an elemnt)
 10. .sort (sort the list)
 11. sorted(method to sort the list)
 12. .reverse(reverse the list)
 13. range(1,10) (make a range from 0 to 9 10 elementh)"""
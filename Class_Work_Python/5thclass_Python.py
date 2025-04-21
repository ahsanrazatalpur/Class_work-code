# LIst in Python  (list is an type of an array that store different type of data)
"""
li = [1, 2, 3, 4, 5, 6]
print(li)
li2 = ['a', 'b', 'c', 'd']
print(li2)
li3 = [1, 4, 7, '4', 'g', 'gh']
print(li3)

cart = ['toys', 'notebook', 'pen', 'laptop']
print(cart)
print(cart[:2])

print(cart[::-1])

cart[0] = "bag"
print(cart)

print(cart[::2])

cart[0] = 340.5
print(cart)
print(type(cart))
print(type(cart[0]))

fruits_cart = ['apple', 'banana', 'grapes'] # remember one thing that startpoint start from zero and endpoint and steppiont start from 1
fruits = fruits_cart[1:3]
print(fruits)

cars = ['civics', 'Mehran', 'honda', 'Cultus']
print(cars)
cars[0] = 'Alto'
print(cars) 

new_cars = cars 
new_cars[1] = 'Thar'
print(new_cars) 
print(cars)

name = ['Ahsan', 'Gull', 'Ayaz', 'Ali']
print(name)
cozn = name[:]
print(cozn)
cozn[0] = 'Hammad'
print(cozn)
# Nested List
matrix = [
    [1, 3, 7, 9],
    [2, 4, 6, 8],
    ['toys', 'book', 'pen', 'usb'],
    [12, 3.4, 'Ahsan', 0, None]
]
print(matrix[0][0], matrix[1][1] , matrix[2][2], matrix[3][3])
matrix[0][0] = 5
matrix[1][1] = 3
matrix[2][2] = 'pencil'
matrix[3][3] = 100
print(matrix[0][0], matrix[1][1] , matrix[2][2], matrix[3][3])
print(type(matrix[3][4]))

# Buil_in Function in List
# 1    .append (add value in the last on list)
number = [1, 23, 100, 99]     # take = number        return = none
print(number)
num = number.append(34)
print(num) # return None
print(number)

# 2      .insert()
marks = [23, 66, 88, 98]    # .insert(index,value) take = value , index   retun = nothing
print(marks)
print(add) # add nothing
print(marks)

# 3  .extend(iterable)   # merge two list   take  = value    return = nothing
science = [34, 88, 90, 100]
art = [98, 44, 78]
print(science)
print(art)
print(science.extend(art)) # return none
print(art.extend(science)) # return none
print(science)
print(art)
print(science.extend([23, 45]))
add = marks.insert(0, 100)
print(science)

# 4  .pop()       .pop(valur) take  = index       return valur
list = [23, 45, 67, 45, 55, 56]
print(list)
print(list.pop(0))
print(list)
toys = ['ball', 'bat', 'ricket', 'cricket']
print(toys)
toys.pop(2)
print(toys)
# 5   .remove()    .remove(value)  take value return nothing
positions = [1, 2, 3, 4, 5]
print(positions)
positions.remove(5) #  it take only one value
positions.remove(2)
print(positions)
names = ['Ahsan', 'Ali', 'mehdi', 'Aizal']
new_names = names.remove('Ahsan')
print(new_names)
print(names)

# 6    .clear()     return nothing use to clear all list list will be clearred , not deleted
sigma = ['mash', 'gojo', 'naruto', 'saloo bhai']
print(sigma)
new_sigmas = sigma.clear()
print(new_sigmas)
print(sigma)

# 7.  .index (value)
number = [12, 34, 56, 78, 56, 67]
number2 = number.index(78) # take value return index
print(number)
print(number2)
print(number.index(12, 0, 3))  # (value , start, end      note: use paranthesis)
print(number2)
print(number.index(0, 0, 5))
 
# 8    .   in keyword
num = [23, 56, 78, 8]
print(23 in num) # if found
print(0 in num) #false

str = "My name is Ahsan raza Talpur"
print('is' in str )  # true

print('name is ' in str )
print('name raza' in str ) # flase

# 9. .count() take value return counting 
number= [23, 45, 67, 666]
print(number.count(6))
print(number.count(45))   

#10     .sort()     take nothing  return none
abc = ['a', 'c', 'r', 'y', 'b']
print(abc.sort())
print(abc)
xyz = [234, 567, 78, 5, 4, 1, 0]
xy = xyz.sort()
print(xyz)
#12 copy list
num = [12, 3, 45, 67, 7]
num2 = num
num2[0] = 9
print(num)
print(num2)
#11    .sorted
list = [23, 45, 56, 67, 0]
list2= sorted(list)
print(list2)

#12 2nd method to copy list
list = [23, 45, 67, 78]
list2 = list[:]
list2[1] = 4
print(list)
print(list2)
# method 3 to copy list
list3 = [23, 45, 67, 78]
list4 = list3.copy()
list4[0] = 66
print(list3)
print(list4)
name = ['aizal', 'mehdi', 'faisal', 'Ali']
name2 = name.reverse()
print(name2)
print(name)
list = [1, 2, 3, 4, 5, 6,  7 ,8, 9]
list.reverse()
print(list)
""" 
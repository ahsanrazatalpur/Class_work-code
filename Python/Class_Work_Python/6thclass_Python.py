"""
basket = ['toys', 'ball', 'bat', 'football']
new_basket = basket[::-1]
print(new_basket)

# Range()
print(range(0,10)) # print as it is print(range(0,10))
print(list(range(0,10)))  # to print range = n-1   list must be written 
print(list(range(0,11)))   #[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# join() only join iterable string ,list, tuple , set and dictinories
x = " "
y = "Ahsan Raza"
z =x.join(y)
print(z)

sep = "_"
name  = "AhsanRazaTalpur"
result = sep.join(name)
print(result)

space = "  "
bio = "MynameisAhsanRazaTalpur"
out = space.join(bio)
print(out)

number = 'OneTwoThree'
spa = " "
p = spa.join(number)
print(p)

#list unpacking

a,b,c = (1, 3, 4)
print(a)
print(b)
print(c)

name,name2,name3 = 'Ali', 'Ahsan', 'Ahmed'
print(name)
print(name2)
print(name3)
a,b,*c = (1, 3, 4, 6, 8)
print(a)
print(b)
print(c) # All remaining item or value will be stored here 

name,fname,*address = ('Ahsan Raza', 'Amir Ali','Village Andhlo City Badin')
print(name)
print(fname)
print(address)
e1,e2,h = 20000, 30000, 20000000
print(e1)
print(e2)
print(h)
a,b,c = 'Ahsan', 1, None  # differenyt value can be stored
print(a)
print(b)
print(c) # None is datatype retrn None
t,f = (True, False)
print(t)
print(f)

#             Dictinory(atriable having value like keys and value) = datastrcucture + cpollection + key + value pair
#             It is mutable inn python
#{
# key : value
# key : value
# key : value
#}
d = {
    'a' : 100, # the elemnts in dictinory doesnot print in sequence in memory 
    'b' : 200,
    'c' : 500

}
print(d)

name  = {
    'Name:' : 'Ahsan Raza',
    'Age:' : '20',
    'Dept' : 'Computer Science'
}
print(name)
r = {
    'a' : 10,
    'b' : 'Ahsan',
    'c' : 'True',
    'd' : 30.9

}
print(r['a'], r['c'])

# value maybe iterable

a = {
 'li' : [1,2,3],
 'li2' : ['A', 'B', 'C']
}
print(a)
print(a['li'])
print(a['li2'])

#Dictinory = unorder(element are not next to each other in the memory) key value pair
# list must have sequence but dictinory doesnot
# Question :  for interview if we print 1000  key value pair does it print in sequence
# Ans : noo, it doesn't because it doesnot print it in sequence in memory so it just print randoml
# y but small size dictinory maybe print or save in memory in sequence
# pyython has different keys for different values
# iterable cannot be key
# if having key of same name will bw overwrited
# key must be imutable

# d = {
#     123 : [1, 2, 3] , # Valid 
#     True : 'Hello', #Valid
#     'abc' : [12, 34, 56], #valid
#    # [1, 3, 4] : '1', '2', '3'  # Not valid

# }
"""

user = {
    'username' : 'ahsanraza',
    'password' : 123
}
print(user.get('username'))
print(user.get(123))
print(user.get('password'))
print(user.get('age',20))
print(user) # Ager value na mili to none return krega


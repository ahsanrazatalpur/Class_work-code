# Tuple
# Tuple are often collection of data type , they store multiple items or values in single variable which is seprated by commas and enclose with round bracket
# Tuple is same as list but it cannot be changed 

# write , even have only one element
tup = (5,)
print(type(tup))
# tup[0] = 1 // got error ,cannot be change 

tup = ( 1, 5, 6) 
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1]) # mean length -1 (3 -1) = 2 index element

tup = (1 ,2 ,3 , "apple" ,"grapes", True,False)
print(len(tup))
print(tup[0])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])

if 3 in tup:
    print("yes 3 is present in tup")
# indexing is posible in tuple but it ren new element
tup2 = tup[:6]
print(tup2)
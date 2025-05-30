# # # # tuple  tuple is same as list but it cannot be changed (imutable)

# # # tup = (10, 20, 30)
# # # print(tup)
# # # print(type(tup))

# # # tup = (10 ,20)
# # # print(tup)
# # # print(type(tup))

# # # tup = (10,)
# # # print(tup)
# # # print(type(tup))

# # # print(list(tup)) # tuple can changed in list

# # #tup[0] = (10,)
# # #print(tup) #TypeError: 'tuple' object does not support item assignment

# # # basket = ('green', 'blue','red')
# # # print(basket)
# # # print(type(basket))

# # # print(basket[0]) # can be acces but cannot be changed
# # # print(basket[1])
# # # print(basket[2])
# # # print(basket[-1])
# # # print(basket[-2])
# # # print(basket[-3])
# # # print(len(basket))

# # # tup = ('red', 'green')
# # # if 'red' in tup:
# # #     print('yes')

# # #----------------------------------------------
# # # slicing
# # tup = (10, 20, 30, 40)
# # tup2 = tup[:2]
# # print(tup2)
# # print(tup)
# #----------------------------------------------------------

# # tuple 
# # add remove insert in tuple you must convert it to list

# countries = ('Pakistan', 'India', 'China', 'Tukry')
# print(countries)
# print(type(countries))
# temp = list(countries)
# print(temp)
# print(type(temp))

# print(temp.append('Iran')) 
# print(temp)
# print(temp.insert(0, 'Pak'))     # .insert(index,value)
# print(temp)

# print(temp.pop(1))             # .pop(index)  return index value
# print(temp)

# print(temp.remove('India')) # remove(value)   return nothing
# print(temp)

# print(temp.sort()) # .sort()  return nothing
# print(temp)

# print(temp.insert(3,'ha')) #return nothing
# print(temp)  

# print(temp.reverse()) # return nothing
# print(temp)

# tup = tuple(temp)
# print(tup)
# print(type(tup))
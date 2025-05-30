# # # # # 1 . Tuple (same as list but imutable)

# # # # t = (10, 20, 30 ,40)
# # # # print(t)
# # # # print(type(t))

# # # # # #t[0] = 30 #nERROR cant assign value
# # # # # #print(t)

# # # # # # t1 = ('A', 'B', 'C', 'D', 'E', 'F')
# # # # # # print(t1)

# # # # # # t3 = (10, 10.8,'abc', True)
# # # # # # print(t3)

# # # # # # add eleemnt at end
# # # tup = (10, 20, 30)
# # # # # # print(tup)

# # # # # # # convert it to list
# # # temp = list(tup)
# # # # # # print(temp)
# # # # # # print(temp.append(100)) #None
# # # # # # print(temp) #[10, 20, 30, 100]

# # # # # # # add at sepcific index
# # # # # new_temp = temp.insert(2,200)#Npne
# # # # # # print(temp)  #[10, 20, 200, 30, 100]

# # # # # # remove item
# # # new_temp = temp.remove(100)
# # # print(temp)

# # # # # remove item at specific index
# # # # new_temp = temp.pop(2) # pop(index)
# # # # print(new_temp) # 200

# # # # #


# # t = (10, 20, 30)
# # li = list(t)

# # # remove(value)
# # newli = li.remove(20)
# # print(newli)
# # print(li)

# # #reverse 
# # rev = li.reverse()
# # print(rev)
# # print(li)

# # #sort
# # print(rev)
# # ne = li.sort()
# # print(ne)
# # print(li)


# # my_tuple = ('apple','bannana','cherry')
# # print(my_tuple[1])

# fruites = ('banana', 'cherry','apple')
# a ,b ,c = 'banana','cherry','apple'
# print(a)
# print(b)
# print(c)

# x ,y ,z = fruites[0],fruites[1],fruites[2]
# print(x)
# print(y)
# print(z)

# # concatenate two tuple
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = [t1,t2]
# print(result)

# tup = (10 ,20, 30 ,40, 50)
# newtup = tup[3:6]
# print(newtup)

# tup = (10, 20, 30 ,40, 50)
# if 20 in tup:
#     print('20 is in tuple')

# # nested tuple
# tup = ('name',('fathername',100))
# print(tup)
# print(tup[1][0])

# info = ('name',('age',20),('language',('python','java')))
# print(info)
# print(info[0][3])

# tup = (10, 20, 30)
# print(type(tup))
# li = list(tup)
# print(type(li))
# newli = li.append(100)
# print(li)

# tu = (i**2 for i in range(5))
# print(tu)

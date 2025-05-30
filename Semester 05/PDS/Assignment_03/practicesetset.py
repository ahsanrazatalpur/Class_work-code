# # # set is well defined unorder collction of data value cannot repeat

# # st = {10, 20, 30, 20, 30}
# # print(st)

# # #union merge two set unorderly
# # s1 = {10 ,20 ,30, 40}
# # s2 = {100, 200, 300, 400}
# # s3 = s1.union(s2) 
# # print(s3)

# # s1 = {10 ,30}
# # s2 = {100, 10, 20, 200}
# # # intersection merge same value
# # s3 = s1.intersection(s2)
# # print(s3)

# # update same as uniom
# # s1 = {10 ,20 ,30}
# # s2 = {0, 12, 20,10}
# # s3 = s1.update(s2)
# # print(s1)

# # # intersection update (same  value update hugi)
# # s2 = {0, 12, 20,10}
# # s1 = {10 ,20 ,30}
# # s3 = s1.intersection_update(s2)
# # print(s3)
# # print(s2)
# # print(s1)

# # s1 = {10 ,20 ,30}
# # s2 = {0, 12, 20,10}

# # #symteric difference differ of s1Us2 - S1nS2 (same / common  nh aigi)
# # s3 = s1.symmetric_difference(s2) 
# # print(s1)
# # print(s2)
# # print(s3)

# # s1 = {10 ,20 ,30}
# # s2 = {0, 12, 20,10}

# # print(s1.symmetric_difference_update(s2)) # 2no mn jo coommon nh
# # print(s1)

# # #isdisjoint dono mn value same na ho ager hugi to false ager nh hui to true
# # s1 = {10 ,20 ,30}
# # s2 = {0, 12, 20,10}
# # print(s1.isdisjoint(s2))

# #issuperset kya ek ke elementb dusre mn hai(sare) ager hainto true else false
# # s1 = {10 ,20 ,30}
# # s2 = {10, 20, 30}
# # print(s1.issuperset(s2))

# # #  .add(value) add an item to set
# # city = {'badin'}
# # city.add('hyderabad')
# # print(city)


# # # discar / remove to delete an item  remove error dega ager eleemnt huga discard error nh dega
# # city = {'badin','hyderabad','karachi'}
# # city.discard('hyderabad')
# # print(city)
# # city.remove('badin')
# # print(city)

# #pop() remove randomn value 
# city = {'badin','hyderabad','karachi'}
# print(city.pop())

# # del keyword to delte
# city = {'badin','hyderabad','karachi'}
# del city
# print(city)


# # # # # # Dictinory
# # # # # dic = {
# # # # #     'Name' : 'Ahsan',
# # # # #     'Age' : 20
# # # # # }
# # # # # print(dic) #{'Name': 'Ahsan', 'Age': 20}

# # # # # data = {
# # # # #     'Name' : 'Ahsan',
# # # # #     'Age' : 20,
# # # # #     'isStudent' : True,
# # # # #     'percentage' : 89.9
# # # # # }
# # # # # print(data)#{'Name': 'Ahsan', 'Age': 20, 'isStudent': True, 'percentage': 89.9}

# # # # #---------------------------------

# # # # bio = {
# # # #     'name' : 'Ahsan',
# # # #     'age' : 20
# # # # }
# # # # print(bio['name']) #Ahsan
# # # # print(bio['age']) #20

# # # # dic2 = {
# # # #     'name' : 'john',
# # # #     10.0 : 'isLucky',
# # # #     'isGood' : True
# # # # }
# # # # print(dic2['name'])
# # # # print(dic2[10.0])
# # # # print(dic2['isGood'])


# # # #--------------------------------------------
# # # dat = {
# # #     'a' : 'hello',
# # #     10 : 'myluvk',
# # #    # ['isGoood','ok'] : 'data' # Error iterable cant be value
# # # }

# # # print(dat['a'])
# # # print(dat[10])
# # # #print(dat['isGoood','ok'])


# # # # iterable can be value but cant be key
# # # dic = {
# # #     'name' : 'Mehdi',
# # #     'age' : 20,
# # #     'bio' : ['isBoy', 'isGood']
# # # }
# # # print(dic)

# # #----------------------------------------------------


# # dat = {
# #     (1, 2) : [10, 20, 30],
# #     'b' : True
# # }
# # print(dat[(1,2)])
# # print(dat['b'])


# # col = {
# #     (10 ,20) : [11, 22, 33],
# #     'bool': True
# # }
# # print(col['bool'])
# # print(col[(10, 20)])

# #@------------------------------------------------

# # dic = {
# #     'basket' : [10 ,20, 30],
# #     'cgpa' : 3.5
# # }
# # print(dic['basket'])
# # print(dic['cgpa'])
# #@------------------------------------------------

# # user = {
# #     'name' : 'xyz',
# #     (10, 20) : (100,200)
# # }
# # print(user['name'])
# # print(user[(10, 20)])
# #@------------------------------------------------

# user = {
#     'name' : 'ali',
#     'caste' : 'talpur'
# }
# print(user.get('age'))
# print(user.get('age',20)) #give default value if key is not  present #20
# #---------------------------------------------------------

# data = {
#     'name' : 'Ahsan',
#     'age' : 20,
#     'occu'  :'student'
#  }
# # print(data['occu'])
# # print(data['age'])
# # print(data['name'])
# # print(data.get('caste')) #None
# # print(data.get('caste','Talpur')) 
# #@------------------------------------------------
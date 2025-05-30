# # List in Python
#List is mutable


# li = [1, 2, 3, 4, 5]
# print(li)
# print(type(li))

# li2 = ['Ahsan', 'Alee', 'Aizal', 'Mehdi']
# print(li2)
# print(type(li2))

# li3 = [20.3, 34.8, 99.3]
# print(li3)
# print(type(li3))

# li4 = ['Ahsan', 34.5, 50, True, None]
# print(li4)
# print(type(li4))
# print(len(li4))

#------------------------------------------

# amazon_cart = ['sunglass', 'bat', 'ball', 'bag']
# print(amazon_cart) #['sunglass', 'bat', 'ball', 'bag']
# new_list = amazon_cart[:2]
# print(new_list)   #['sunglass', 'bat']
# print(amazon_cart) #list cannot be changed

#-------------------------------------------

# amazon_cart = ['sunglass', 'bat', 'ball', 'bag', 'dress']
# print(amazon_cart)

# amazon_cart[0] = 'gucii'
# print(amazon_cart)  # list can be change ['gucii', 'bat', 'ball', 'bag', 'dress']

# amazon_cart[1] = 10.43
# print(amazon_cart) #['gucii', 10.43, 'ball', 'bag', 'dress']

# print(type(amazon_cart[1]))

#------------------------------------------------------------------------

#  list slicing 

# amazon_cart = ['sunglass', 'bat', 'ball', 'bag', 'dress']
# print(amazon_cart[0:len(amazon_cart)])
# print(amazon_cart[2:4]) #'ball', 'bag'
# print(amazon_cart[::-1]) #'dress', 'bag', 'ball', 'bat', 'sunglass'

# new_list = amazon_cart[:2]
# print(new_list)

#------------------------------------------------------------------------
#----------------------------------------------
# amazon_cart = ['dress', 'bag', 'ball', 'bat', 'sunglass']
# amazon_cart[0] = 'mobile'
# newCart = amazon_cart
# newCart[0] = 'lipstick'
# print(newCart)
# print(amazon_cart)

#----------------------------------------------

# amazonCart = ['lipstick', 'bag', 'ball', 'bat', 'sunglass']
# newCart = amazonCart[::]
# newCart[0] = 'Doll'
# print(newCart)
# print(amazonCart)

#----------------------------------------------

# matrix = [
#     [10, 20, 30],
#     [True,False],
#     [10.7,923.5],
#     ['Hi', 'Bye']
    
#     ]
# print(matrix[0][0]) #10
# print(matrix[1][1]) #False
# print(matrix[3][0]) #Hi

#----------------------------------------------

# List Methods

# #1   .append(value) add value at last 
# # return nothing but add value in origrinal 
# li = [10, 20, 30]
# print(li)
# print(len(li))
# newList =  li.append(100) # add value at last
# print(newList) # add value but return nothing
# print(li)

# basKet = ['ball', 'Dol', 'toys']
# print(basKet)
# basKet.append('car') #['ball', 'Dol', 'toys']
# print(basKet) #['ball', 'Dol', 'toys', 'car']

#----------------------------------------------

# 2 .insert(index,value) return none
# basket = ['ball' , 'bat', 'Hockey']
# print(basket) #['ball', 'bat', 'Hockey']
# basket.insert(1,'jeep') 
# print(basket)#'ball', 'jeep', 'bat', 'Hockey'
#----------------------------------------------
# 3 .extend(iterable) return nothing
# basket = ['toys', 'car','ball']
# print(basket)
# newbasket = basket #['toys', 'car', 'ball']
# print(newbasket) #['toys', 'car', 'ball']
# newbasket =['bet', 'jeep']
# newbasket.append(basket)
# print(newbasket)
# basket = ['toys', 'car', 'ball']
# basket.extend(['toyota','suzuki'])
# print(basket)
#----------------------------------------------

# 4.pop(index) return value at index
# number = [1 ,2, 3, 4, 5,]
# print(number)#1,2,3,4,5
# number.pop(0)
# print(number)# 2,3,4,5
# a =number.pop(2)
# print(number)# 2,3,5
# print(a) #4



# #----------------------------------------------

#  5.remove(value) return None
# num = [1, 2, 3, 4, 6]
# print(num)
# new = num.remove(2)
# new = num.remove(6)
# print(num) # 1,2,4,5
# print(new) # None

# if we have same value twice it will remove first occurence
# num = [10, 20, 10, 29]
# num.remove(10)
# print(num)
# #----------------------------------------------

# 6 .clear() clear all the list return None
# basket =[10, 20, 30, 40]
# a = basket.clear()
# print(a) # None
# print(basket) # [] clear all list
# #----------------------------------------------
# .index(value) return index
# value or value,start,end

# a = basket = [12, 20, 30, 40]
# print(basket.index(30)) #2
# print(a) #[12, 20, 30, 40]
# #print(basket.index(30,0,1)) #ValueError: 30 is not in list
# print(basket.index(30,0,3))

# #----------------------------------------------

# lis = ['a', 'b', 'c', 'd','b']
# print(lis)
# print('d' in lis) #true
# print('i' in 'my name is Ahsan') #true

# print(lis.count('b')) #2

#-----------------------------------------------------
#  7 .sort() sort the data and return None
# abc = ['a' ,'e', 'c', 'd', 'b']
# print(abc.sort())
# print(abc)

# num = [9,8,7,6,4,5,7,3,2,1,0]
# print(num.sort())
# print(num)
# print(num.count(7))
# print(7 in num)

#-----------------------------------------------------
# to copy list
# num = [1, 2, 3 ,4, 5, 6 ,7]
# new = num
# num[0] = 100
# print(num) #[100, 2, 3, 4, 5, 6, 7]
# print(new)# [100, 2, 3, 4, 5, 6, 7]

# num = [1, 2, 3 ,4, 5, 6 ,7]
# new = num[:]
# num[0] = 100
# print(num) #[100, 2, 3, 4, 5, 6, 7]
# print(new)# [1, 2, 3, 4, 5, 6, 7]

# num = [1, 2, 3 ,4, 5, 6 ,7]
# new = num.copy()
# num[0] = 100
# print(num) #[100, 2, 3, 4, 5, 6, 7]
# print(new) #[1, 2, 3, 4, 5, 6, 7]

# #-----------------------------------------------------
# num = [10, 20, 30, 40, 50]
# print(num.reverse()) #None
# print(num) #[50, 40, 30, 20, 10]
# #-----------------------------------------------------
# # shorthand methods trick

#  .append() add element at the end of list                                    return None
#  .extend(iterable) merge two lits/itreable                                   return None
#  .insert(index,value) add an element at position                             return None
#  .remove(value) remove first occurence of value                              return None
#  .pop(index) remove eleemt at index (default last)                           return removed element
#  .clear() clear all the list                                                 return None
#  .index(value) return the index of first occurence                           return index
#  count(value) count the given value                                          number of value
#  .sort() sort the list                                                       None
#  .reverse() reverse the list                                                 None
#  copy() copt the element of list                                             new list(copy)

# #-----------------------------------------------------------
# # to reverse the patter
# li1 = [1 ,2 ,3, 4, 5]
# newLi = li1[::-1]
# print(newLi)

# # range
# print(range(0,10)) #range(0, 10)
# print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(11))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #-----------------------------------------------------------
# # to reverse the patter
# li1 = [1 ,2 ,3, 4, 5]
# newLi = li1[::-1]
# print(newLi)

# # range
# print(range(0,10)) #range(0, 10)
# print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(11))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# #-----------------------------------------------------------
# #-----------------------------------------------------------
# a = ['my','name','is','ahsan']
# print(a)
# b =''
# c = a.join(b);
# print(c)
# #-------------------------------------------------------------------
# a ,b, c = 10,20,30
# print(a)
# print(b)
# print(c)

# a, b, c, d = 'hi','bye','dye', 'hehe'
# print(a)
# print(b)
# print(c)
# print(d)

# a ,b, *c = 1,2,3,4,5,6,78
# print(a) #1
# print(b) #2
# print(c) #[3, 4, 5, 6, 78]

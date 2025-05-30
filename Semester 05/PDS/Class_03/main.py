# #String slicing 
# # string are imutable , cannot changed once its created
# # [start:end:step]
# x = '34342'
# print(x)
# print(type(x))
# print(len(x))

# #x[0] = '3' sttring canot assign the  value
 
# print(x + '35462') # only way to assign value in string
# x = x + 'u3u43' in this case whole string new
# print(x) # new string

# a = 'hello'
# print(a)
# print(type(a))
# print(len(a))

#  greet='helooooo'
# print(greet)
# print(len(greet))

# print(greet[:]) # whole string
# greet ='helooooo'
# print(greet[0:]) # whole  string
# print(greet[0:len(greet)]) # whole  string

# print(greet[0:5]) # substring

#-----------------------------------------------

# String built in function 

# #.replace('old' , 'new')
# # it return new modified string its doesnot change original string because string is imutable and it doesnot return null as well
# intro = 'Hey mr, how are you'
# print(intro)
# print(intro.replace('mr','ahsan'))
# print(intro) # oroginal string bc string cannot be change 

# myintro = intro.replace('mr','Alee')
# print(myintro)
# print(intro)

#----------------------------------------------------\
# # .lower()  all lower character
# quote = 'Never loose hope !'
# print(quote.lower())

# # .upper() all upper character
# print(quote.upper())

# # .capitalize()  # first letter capital
# print(quote.capitalize())

# # .find('char')
# print(quote.find('hope')) #12 return index before target
# print(quote.find('loose'))
# print(quote.find('p'))

# find,replace,upper(),lower(),capitilaize doest effect original string it return modified string
#and also doesnot return null


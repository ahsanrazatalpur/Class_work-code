#    Set
# Sets are unorderd collection of data items.They store multiple item in single variable with the single occurence set items are seprated by commas and inclosed in curly bracket. Set are unchangable and does not contain duplicate item


st = {2 ,2, 4, 5, 2}
print(st)

# item ek bar occur hoga but order ki koi gurrenty nh 4 pehle b aaskta bad mn b 
st = {1 ,4, 5, "set" , "oop", 4 , 9}
print(st)

print(type(st))
# print(st[0]) hum set ko element ko index se call nh ker sakte because order ki koi gurenty nh

# empty = {}  it  create empty dictinory not empty set
#print(type(empty))

# we can create empty set like this
empty = set()
print(type(empty))

for element in  st:
    print(element)

# Methods in Set 

# union (merge two sets)
s1  ={1 ,2 ,3}
s2 = {2 ,4, 6}
print(s1.union(s2))

# intersection (return same element in both sets)
s1  ={1 ,2 ,3}
s2 = {2 ,4, 6}
print(s1.intersection(s2))

# update ( update value or add value )
print(s1,s2)
s1.update(s2)
print(s1)

# intersection update(update same value present in both sets)
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","badin","sakhar"}
s1.intersection_update(s2)
print(s1)

# symetric difference(return value which are not common in both set
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","badin","sakhar"}
s3 = s1.symmetric_difference(s2)
print(s3)

#difference(the difference of both set s1 mn wo value kat jaegi jo s2 mn bhi n ha )
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","badin","sakhar"}
s3 = s1.difference(s2)
print(s3)

# isdisjoint(no common value present in both sets 
# if present than false else true)
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","badin","sakhar"}
s3 = s1.isdisjoint(s2)
print(s3)
# return true bcause no commone element in below set
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","kadhan","sakhar"}
s3 = s1.isdisjoint(s2)
print(s3)

# issuperset(kya set 1 ke element set 2 mn hain)
s1 = {"badin","hyd", "karachi"}
s2 = {"golarchi","kadhan","sakhar"}
s3 = s1.issuperset(s2)
print(s3)
s1 = {"badin","hyd", }
s2 = {"hyd","badin"}
s3 = s1.issuperset(s2)
print(s3)
# issubset(kya ek ke element dusre mn hai)
s1 = {"badin","hyd", }
s2 = {"hyd","badin"}
s3 = s1.issubset(s2)
print(s3)

# remove (remove any element from set but through error)
cities = {"hyd", "badin"}
cities.remove("badin")
print(cities)

# discard (remove item but doesnot throgh error)
cities = {"hyd", "badin"}
cities.discard("badin")
print(cities)

# pop (remove any randomn element)
cities = {"hyd", "badin","karachi", "golarchi"}
item = cities.pop()
print(cities)
print(item)

# del (delete cities)
cities = {"hyd", "badin","karachi", "golarchi"}
del cities
 # print(cities) cities is del so cant print
 
 # clear (claer all set return empty set)
cities = {"hyd", "badin","karachi", "golarchi"}
cities.clear()
print(cities)

names = {"ahsan", "ali", "gull" }
if "ahsan" in names:
    print("Ahsan is present")
else:
    print("not present")

# # Set (collection of well defined unorder data and non-repeating item)
# # order doesn't matter in set and unchangable

# st = {10, 20, 30, 20}
# print(st)
# print(type(st))

# # print(st[0]) #ERROR bc set is unorder

# empty = set()
# print(empty)
# print(type(empty))

# for value in st:
#     print(value)

st1 = {10, 20 ,30, 40}
st2 = {50, 60, 70, 80}

# union all item merge
print(st1.union(st2))

#intersection merge same element in bth set
print(st1.intersection(st2))

# update ek ki value dusre mn le ao
print(st1.update(st2)) #return none
print(st1)
st1={10,20,10} 
st2 = {100,10,29}
print(st1.intersection_update(st2)) #None

# wo values jo common nh ahi
print(st1.symmetric_difference(st2))

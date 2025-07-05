name ="parimal"
last = "patel"











# lst = [1, 2, 3, 4, 5]
# print("len of list:-",len(lst))
# print("type of list:-",type(lst))
# #indexing
# print(lst[0])
# print(lst[4])
# #slicing
# print(lst[0:4])

# #element add in list
# lst.append(400)
# print(lst)
# #element remove in list
# lst.pop()
# print(lst)
# lst.pop(3)
# print(lst)

# #element add at specific loaction
# lst.insert(2,10)
# print(lst)
# lst.clear()
# print(lst)

# # reversing the list
# lst = [1, 2, 3, 4, 5]
# lst.reverse()
# print(lst)

# # count the elements
# print(lst.count(1))
# # sort the list
# lst.sort()
# print(lst)

# copy the list
#deep copy
#copy

# TUPLES
# tup = (1,23,4,4,5,5,"parimal",2.25)
# print("type of tuple:-",type(tup))
# print("len of tuple:-",len(tup))
# #indexing
# print(tup[6])
# print(tup[3])

# #slicing
# print(tup[0:7])
# print(tup[-1:4:-1])
# print(tup[::-1])
# tup1=(1,2,3,4,5)
# print(max(tup1))
# print(min(tup1))
# tple =(1,2,3,5,4,8,8,[1,2,7,8])
#tple=(8[2,3])
# print(tple[6][2])
#print(tple[6][2])

#dictionary
# dct = {
#     "name": "parimal",
#     "age" :20, "city" :"surat"
# }
# print("type of dictionary:-",type(dct))
# print(dct["name"])
# print(dct["age"])
# print(dct["city"])
# print(dct.get("name"))

# #adding key and value
# dct['address'] ="jaipur"
# print(dct)
# #update the value of key
# dct['age'] = 21
# print(dct)
# #variablename.update(key,value)

# #delete the key and value
# del dct['city']
# print(dct)
# #pop the key and value
# dct.pop('name')
# print(dct)
# print(dct.keys())
# print(dct.values())
# print(dct.items())
# print("address" in dct)

#set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("type of set:-", type(s))
print(s)
#add function
s.add(100)
print(s)
#remove function
s.remove(100)
print(s)

s.discard(100)  # does not raise an error if the element is not found
print(s)  
#union
#intersection
#difference
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(mylist))
print(mylist)
myset = set(mylist)
print(type(myset))
print(myset)
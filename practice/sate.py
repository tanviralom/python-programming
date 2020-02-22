set_1 ={1,3,5,7,9}
print(set_1)
print(type(set_1))

#add single item
print(set_1.add(2))
print(set_1)

#add multiple  items
set_1.update([12,34,78])
print(set_1)

#remove item
set_1.remove(78)
print(set_1)

#unic operator
set_2 = {100,100,200}
print(set_1 | set_2)

#intersection
print(set_1 & set_2)

#to clear
set_1.clear()
print(set_1)

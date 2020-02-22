lst=[10,34,23,45,789]
lst1=[x for (i,x) in enumerate(lst) if i not in(0,4,5)]
print(lst1)
print(lst)
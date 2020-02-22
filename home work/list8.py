lst1=['dipu','antu','shourav','farhan']
lst2=['arman','towfiq','habib','sakib']
lst3=[]
lst3.extend(lst1)
lst3.extend([lst2])
print(lst3)
lst1.extend(lst2)
print(lst1)
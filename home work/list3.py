lst=['dipu','antu','assa','1221']
n=0
for i in lst:
    if len(i)>1 and i[0]==i[-1]:
        n+=1;

print(n)
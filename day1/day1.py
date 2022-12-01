f = open("input.txt","r")
lines = f.readlines()
current=0
list=[]
for i in range(len(lines)):
    print(lines[i])
    print(i)
    if lines[i]=="\n":
        list.append(current)
        current=0;
    else:
        current+=int(lines[i])
list.sort()
sum=list[-1]+list[-2]+list[-3]
print(sum)
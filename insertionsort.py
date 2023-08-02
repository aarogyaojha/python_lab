nlist=[]
n=int(input("enter the number"))
for i in range(n):
    num=int(input())
    nlist.append(num)

for i in range(1,n):
    j=i
    picked=nlist[i]
    while j>0 and picked<nlist[j-1]:
        nlist[j]=nlist[j-1]
        j=j-1
    nlist[j]=picked
print(nlist)
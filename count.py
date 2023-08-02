line=input("Enter a sentence").split()
count=0
countdig,countele,countlow,countupper=0,0,0,0
for x in line:
    count=count+1
    for y in x:
        countele=countele+1
        if(y.upper()):
            countupper=countupper+1
        elif(y.lower()):
            countlow=countlow+1
        else:
            countdig=countdig+1
        
    
print(count,countupper,countele,countlow)
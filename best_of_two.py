test1=int(input("enter the first test marks"))
test2=int(input("enter the second test marks"))
test3=int(input("enter the third test marks"))
total=test1+test2+test3
best_of_2=total-min(test1,test2,test3)
avg=best_of_2/2
print(avg)
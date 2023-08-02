num = int(input("enter the number to check"))
temp = num
freq = {}
sum = 0
while num != 0:
    rem = num % 10
    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1
    sum = sum * 10 + rem
    num = num // 10
if sum == temp:
    print("Palindrome")
else:
    print("not")

print(freq)
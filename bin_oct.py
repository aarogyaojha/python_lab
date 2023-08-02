def bin_to_dec(bin):
    dec=0
    power=0
    while(bin!=0):
        rem=bin%10
        dec=dec+rem*2**power
        bin=bin//10
        power=power+1
    return dec

def oct_to_hex(num):
    n=int(num,8)
    hexa=hex(n)
    return hexa



bin=int(input("enter number in binary"))
print(bin_to_dec(bin))

oct=input("enter the number in octal")
num='0o'+oct
print(oct_to_hex(num))
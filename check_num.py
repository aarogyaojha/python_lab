import re

def validate(s):
    return bool(re.search('^\d{3}-\d{3}-\d{4}',s))

def validate2(s):
    if(len(s)!=12):
        return False
    for i in range (len(s)):
        if i==3 or i==7:
            if(s[i]!="-"):
                return False
        else:
            if not s[i].isdigit():
                return False
    return True

s=input("enter phone number")
print("Using re")
result=validate(s)
if(result):
    print("valid")
else:
    print("not")


print("Without Using re")
res=validate2(s)
if(res):
    print("valid")
else:
    print("not")


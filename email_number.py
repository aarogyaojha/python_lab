import re

mytext = open("D:/python/lab/abc.txt").read()
print(mytext)

phoneregex = re.compile(r"\d{12}")
result = re.findall(phoneregex, mytext)
print(result)

emailregex = re.compile(r"""[a-zA-Z0-9._+%-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}""", re.VERBOSE)
matches = emailregex.findall(mytext)

print(matches)

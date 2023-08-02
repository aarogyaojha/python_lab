import difflib

def similarity(s1,s2):
    result=difflib.SequenceMatcher(a=s1.lower(),b=s2.lower())
    return result.ratio()


a=input()
b=input()
print(similarity(a,b))
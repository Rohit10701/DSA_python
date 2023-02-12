
def valid(s):
    for i in range(2,len(s)):
        if len(s)==1:
            return False
        if s[i]==s[i-1]:
            return False
        if s[i]!=s[i-2]:
            return False
    return True
def alternate(s):
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            s.remove(s[i])
    #bcdbd
    #bagbfabagf
    stack=[]
    i=0
    while True:
        if stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            

print(alternate('abaacdabd'))
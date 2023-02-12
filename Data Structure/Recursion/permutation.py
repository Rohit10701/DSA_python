def permu(s,temp,ls):
    if len(s)==0:
        ls.append(temp)
        return
    else:
        for i in range(len(s)):
            permu(s[:i]+s[i+1:],temp+s[i],ls)
            
    return ls

print(permu("abc","",[]))

#"abc"
# "",a,b,c,ab,bc,ca,abc
#['abc','ab','ac','a','bc','b','c','']
def combi(s,temp,ls):
    for i in range(len(s)):
        sorted_word = sorted(temp)
        sorted_word = ''.join(sorted_word)
        if sorted_word not in ls:
            ls.append(sorted_word)
        combi(s[:i]+s[i+1:],temp+s[i],ls)     
    return ls+[s]

print(combi("bccb","",[]))
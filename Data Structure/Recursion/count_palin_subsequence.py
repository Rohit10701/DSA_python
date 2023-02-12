from email.errors import CloseBoundaryNotFoundDefect


def valid(s):
    if s=='':
        return False
    if s==s[::-1]:
        return True
    return False

def combi(s,temp,ls):
    for i in range(len(s)):
        
        if temp not in ls:
            ls.append(temp)
        combi(s[:i]+s[i+1:],temp+s[i],ls)     
    return ls+[s]


def countPalindromicSubsequences(s: str) -> int:
        ls=[]
        combi(s,"",ls)
        ls=ls+[s]
        count=0
        for ele in ls:
            if valid(ele):
                count+=1
        return count%(10**9+7)

print(countPalindromicSubsequences("bccb"))
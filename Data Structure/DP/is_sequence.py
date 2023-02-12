def isSubsequence(s, t):
        i=1
        while(len(s)>0 and len(t)>0):
            a=s[0]
            b=t[0]
            if s[0]==t[0]:
                s=s[i:]
                t=t[i:]
            else:
                t=t[i:]
        if len(s)==0:
            return True
        else:
            return False

print(isSubsequence("abc","adbec"))

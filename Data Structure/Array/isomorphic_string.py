def isIsomorphic(s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        hm_f={}
        hm_b={}

        for i in range(len(s)):
            if s[i] not in hm_f:
                hm_f[s[i]]=t[i]
        
        for i in range(len(t)):
            if t[i] not in hm_b:
                hm_b[t[i]]=s[i]

        str_f=""
        str_b=""
        for i in range(len(s)):
            if s[i] not in hm_f:
                return False
            str_f = str_f + hm_f[s[i]]
        print(str_f)

        for i in range(len(t)):
            if t[i] not in hm_b:
                return False
            str_b = str_b + hm_b[t[i]]
        print(str_b)

        if str_f == t and str_b == s:
            return True
        return False

print(isIsomorphic("abab","baba"))
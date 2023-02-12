def sqSum(num):
    strs=str(num)
    res=0
    i=0
    while i<len(strs):
        res=res+(int(strs[i]))**2
        i+=1
    return res

def isHappy( n: int) -> bool:
    hm={}
    hm[n]=1
    val=sqSum(n)
    while val!=1:
        if val in hm:
            return False
        else:
            hm[val]=1
        val=sqSum(val)
    return True

print(isHappy(17))
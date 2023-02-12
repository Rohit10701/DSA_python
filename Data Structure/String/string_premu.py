from math import perm

ls=[]
def permu(strs:str,ans):
    if len(strs)==0:
        ls.append(ans)
        return
    else:
        for i in range(len(strs)):
            ch=strs[i]
            lsub=strs[0:i]
            rsub=strs[i+1:]
            rest=lsub+rsub
            permu(rest,ans+ch)

strs="abc"
permu(strs,"")
print(ls)
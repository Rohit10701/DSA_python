
def subset(str,res,depth,ls):
    if depth==len(str):
        ls.append(res)
        return
    subset(str,res+[str[depth]],depth+1,ls)
    subset(str,res,depth+1,ls)
    return

ls=[]
print(subset([-1,2,3],[],0,ls))
print(ls)


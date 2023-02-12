def comb(nums,k,temp,res,depth):
    if len(temp)==k:
        res.append(temp)
        return
    if depth<len(nums):
        comb(nums,k,temp+[nums[depth]],res,depth+1)
    if depth<len(nums):
        comb(nums,k,temp,res,depth+1)
    return
n=4
nums=[n+1 for n in range(n)]
res=[]
k=2
comb(nums,k,[],res,0)
print(res)
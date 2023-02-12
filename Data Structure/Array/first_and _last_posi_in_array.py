def bSearch(nums,start,end,target,ls):
    if len(nums)==0:
        ls=[-1,-1]
        return ls

    mid = (start+end)//2
    if mid==end or mid==start:
        if nums[mid]!=target:
            ls=[-1,-1]
            return ls
    
    
    if target == nums[mid]:
        left=mid
        right=mid

        while nums[left]==nums[mid]:
            left-=1
        ls.append(left+1)
        while nums[right]==nums[mid]:
            right+=1
        ls.append(right-1)
        return ls
    
    if target < nums[mid]:
        bSearch(nums,start,mid,target,ls)
        
    if target> nums[mid]:
        bSearch(nums,mid,end,target,ls)
ls=[]
nums=[1]
print(bSearch(nums,0,len(nums),0,ls))
print(ls)
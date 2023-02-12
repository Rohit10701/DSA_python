def CloSum(nums,target):
    nums.sort()
    #[-4,-1,-1,0,1,2]
    ans=[]
    res=0
    for i,ele in enumerate(nums):
        if i>0 and ele==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            threeSum=ele+nums[l]+nums[r]
            if threeSum>target:
                r-=1
                ans.append(threeSum)
            elif threeSum<target:
                l+=1
                ans.append(threeSum)
            else:
                ans.append(threeSum)
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    min_diff=999999999
    sum=0
    for i,ele in enumerate(ans):
        diff=abs(target-ele)
        if min_diff>diff:
            sum=ele
    return  sum

print(CloSum(,))
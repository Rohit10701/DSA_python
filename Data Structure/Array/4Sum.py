def fourSum(nums, target):
        nums.sort()
        print(nums)
        ls=[]
        l,r=0,len(nums)-1
        mid=1
        while mid<r:
            while mid<r:
                val=target-(nums[l]+nums[r]+nums[mid])
                if val in nums[mid+1:r]:
                    ls.append(sorted([nums[l],nums[r],nums[mid],val]))
                    mid+=1
                
            l+=1
            mid=l+1
            r=len(nums)-1
        return ls

print(fourSum([1,0,-1,0,-2,2],0))
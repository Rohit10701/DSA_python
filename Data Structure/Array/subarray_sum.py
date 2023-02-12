def subsum(nums,k):
        i=0
        j=0
        sum=0
        count=0
        while i<len(nums) or j<len(nums):
            sum=sum+nums[i]
            
            if sum==k:
                count+=1
                j+=1
                i=j-1
                sum=0
            if i==len(nums)-1:
                sum=0
                j+=1
                i=j-1
            i+=1
            
        return count

print(subsum([1,-1,0],0))
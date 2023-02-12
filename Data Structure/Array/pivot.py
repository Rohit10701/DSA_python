def pivotIndex(nums) -> int:
        left_sum=0
        right_sum=0
        
        total_sum = sum(nums)
        for i in range(len(nums)):
            if i>=1:
                left_sum = left_sum + nums[i-1]
            if i<len(nums)-1:
                right_sum = total_sum - nums[i] - left_sum
            else:
                right_sum=0
            if left_sum == right_sum:
                return i
        return -1

print(pivotIndex([2,1,-1]))
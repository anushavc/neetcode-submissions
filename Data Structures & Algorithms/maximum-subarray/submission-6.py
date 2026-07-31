class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute Force
        max_sum=nums[0]
        for i in range(len(nums)):
            running_sum=0
            for j in range(i,len(nums)):
                running_sum=running_sum+nums[j]
                max_sum=max(max_sum,running_sum)
        return max_sum

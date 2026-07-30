class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum=nums[0]
        running_sum=nums[0]
        for i in range(1,len(nums)):
            if running_sum<0:
                running_sum=nums[i]
            else:
                running_sum=running_sum+nums[i]
            maximum_sum=max(maximum_sum,running_sum)
        return maximum_sum
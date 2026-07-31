class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #optimized (we dont want to add a sum that it is negative)
        running_sum = nums[0]
        maximum_sum = nums[0]
        for i in range(1, len(nums)):
            running_sum = max(nums[i], running_sum + nums[i])
            maximum_sum = max(maximum_sum, running_sum)
        return maximum_sum


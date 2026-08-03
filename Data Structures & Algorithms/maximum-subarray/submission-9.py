class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #find subarray with the largest sum and return the sum
        """
        nums=[2,-3,4,-2,2,1,-1,4]
        to find the largest sum, the logic is kadane's algo
        if an element that you are adding is making it negative, we start new, if it is not, then add to the sum. we are tracking the running_sum and the max_sum
        """
        running_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            running_sum=max(nums[i],running_sum+nums[i])
            max_sum=max(max_sum,running_sum)
        return max_sum


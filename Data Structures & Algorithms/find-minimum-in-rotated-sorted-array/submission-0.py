class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num=nums[0]
        for i in nums:
            min_num=min(min_num,i)
        return min_num


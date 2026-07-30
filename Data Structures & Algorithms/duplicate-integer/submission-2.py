class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sorting the array and one pass
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
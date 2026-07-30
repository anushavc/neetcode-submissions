class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #finding duplicate
        #we have an array [1,2,3,3]
        #we can create a hashmap which has the bool value if we have seen it before
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

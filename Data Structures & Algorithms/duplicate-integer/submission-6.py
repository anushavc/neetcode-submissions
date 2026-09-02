class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset to put the element and check if the element has been seen before
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
       
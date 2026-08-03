class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimized solution - hashmap
        #redo
        hashmap={}
        for i in range(len(nums)):
            #we are searching if we have seen the complement previously in the hashmap
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            else:
                hashmap[nums[i]]=i
        
        

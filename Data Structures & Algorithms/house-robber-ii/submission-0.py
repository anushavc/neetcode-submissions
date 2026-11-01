class Solution:
    def rob(self, nums: List[int]) -> int:
        #the base of this code involves two potential directions: without house 0 and without house 3
        if len(nums)==1:
            return nums[0]
        #without house 0
        street_a=nums[1:]
        #without the last house
        street_b=nums[:-1]
        return max(self.helper(street_a),self.helper(street_b))

    def helper(self,nums):
        if len(nums)==1:
            return nums[0]

        #running total
        best=[0]*len(nums)
        best[0]=nums[0]
        best[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            best[i]=max(best[i-1],nums[i]+best[i-2])
        return best[-1]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search approach
        l=0
        r=len(nums)-1
        while l<r:
            #computing the midpoint of the array 
            mid=(l+r)//2
            #if midpoint is higher than the r
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[r]
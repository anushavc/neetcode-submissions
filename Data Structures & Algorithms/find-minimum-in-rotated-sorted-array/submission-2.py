class Solution:
    def findMin(self, nums: List[int]) -> int:
        #optmized Solution
        #binary search
        """
        [3,4,5,6,1,2]
        we divide into high and low chunks
        high chunk: [3,4,5,6]
        low chunk: [1,2]
        we are trying to check the element that we are parsing the midpoint:
        if the midpoint is greater than the rightmost element:
            then we know that this element is in the high chunk so we want to go towards the right to search
            (left=mid+1)
        if the midpoint is lesser or equal to the rightmost element:
            then we know that this element is in the low chunk so we want to go towards the left to search
            (right=mid)
        """
        left_pointer=0
        right_pointer=len(nums)-1
        while left_pointer<right_pointer:
            midpoint=(left_pointer+right_pointer)//2
            if nums[midpoint]>nums[right_pointer]:
                left_pointer=midpoint+1
            else:
                right_pointer=midpoint
        return nums[left_pointer]

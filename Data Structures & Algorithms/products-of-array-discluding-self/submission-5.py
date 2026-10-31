class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array=[]
        right_array=[]
        resultant_array=[]

        running_product=1
        #left hand side array
        for i in nums:
            left_array.append(running_product)
            running_product=running_product*i
        
        running_product=1
        for i in range(len(nums)-1,-1,-1):
            right_array.append(running_product)
            running_product=running_product*nums[i]
        for i in range(0,len(nums)):
            resultant_array.append(left_array[i]*right_array[len(nums)-i-1])
        return resultant_array

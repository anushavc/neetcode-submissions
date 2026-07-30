class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array=[]
        right_array=[]
        output=[]
        left_product=1
        right_product=1
        for i in range(0,len(nums)):
            left_array.append(left_product)
            left_product=left_product*nums[i]
        for i in range(0,len(nums)):
            right_array.append(right_product)
            right_product=right_product*nums[len(nums)-1-i]
        print(left_array)
        print(right_array)
        for i in range(0,len(nums)):
            output.append(left_array[i]*right_array[len(nums)-i-1])
        return output
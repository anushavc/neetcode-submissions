class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        res_array=[]
        for i in range(0,len(nums)):
            running_product=1
            for j in range(0,len(nums)):
                if i!=j:
                    running_product=running_product*nums[j]
            res_array.append(running_product)
        return res_array

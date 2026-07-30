class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating result array
        result=[1]*len(nums)
        product=1
        for i in range(0,len(nums)):
            #internal product
            for j in range(0,len(nums)):
                if i!=j:
                    product=nums[j]*product
            result[i]=product
            product=1
        print(result)
        return result

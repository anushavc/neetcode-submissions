class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solution-two passes- O(1) pass
        output=[1]*len(nums) #output length of n to store

        #filling output with prefix values
        pre=1
        for i in range(0,len(nums)):
            #first update the array
            output[i]*=pre
            #multiply
            pre*=nums[i]
            
        #filling output with suffix values
        suf=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=suf
            suf*=nums[i]
        return output


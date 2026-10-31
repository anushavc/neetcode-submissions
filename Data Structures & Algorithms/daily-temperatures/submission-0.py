class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create the monotonic decreasing stack
        stack=[]
        result=[0]*len(temperatures)

        for i,t in enumerate(temperatures):
            #if the tempature is lesser than previous one, add to the stack
            #if i is greater, we pop the temp from the stack and calculate the index difference and put into the result
            while stack and t>temperatures[stack[-1]]:
                j=stack.pop()
                result[j]=i-j
            stack.append(i)
        return result

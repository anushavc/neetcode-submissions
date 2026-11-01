class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       cost.append(0) #here we add the top step
       for i in range(len(cost)-3,-1,-1):
        cost[i]+=min(cost[i+1],cost[i+2])#cost of 1 step or step 2 added to the running ottal of being on that step
       return min(cost[0],cost[1]) 
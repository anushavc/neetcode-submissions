import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        num=[1,2,2,3,3,3]
        k=2
        #heap based solution
        """
        count=Counter(nums)
        #now we create a list which is the length of the nums
        buckets = [[] for _ in range(len(nums) + 1)] 
        for num,freq in count.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(buckets) - 1, 0, -1): 
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res


        
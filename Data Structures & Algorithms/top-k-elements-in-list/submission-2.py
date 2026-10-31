import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        num=[1,2,2,3,3,3]
        k=2
        #heap based solution
        """
        #we need to find the counts of the array
        hashmap=defaultdict()
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        ordered=sorted(hashmap, key=hashmap.get, reverse=True)
        return ordered[:k]
        


        
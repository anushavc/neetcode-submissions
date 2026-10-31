from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """DefaultDict, 
        strs = ["act","pots","tops","cat","stop","hat"]
        Solution 2: Optimized (instead of sorting the word for the key, using a constant occurences of characters in the word)
        """
        group=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            group[tuple(count)].append(s)
        return list(group.values())
        

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """DefaultDict, 
        strs = ["act","pots","tops","cat","stop","hat"]
        Solution 2: Optimized (instead of sorting the word for the key, using a constant occurences of characters in the word)
        """
        groups=defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')]+=1
            groups[tuple(count)].append(i)
        return list(groups.values())
        

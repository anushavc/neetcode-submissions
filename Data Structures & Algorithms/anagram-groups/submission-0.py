from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """DefaultDict, 
        strs = ["act","pots","tops","cat","stop","hat"]
        Solution 1: Sorting the words and using those as a key 
        """
        groups=defaultdict(list)
        for i in strs:
            #create the key
            key="".join(sorted(i))
            #add the word to the key
            groups[key].append(i)
        return list(groups.values())        


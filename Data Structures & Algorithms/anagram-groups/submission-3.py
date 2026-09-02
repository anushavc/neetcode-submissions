from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["act","pots","tops","cat","stop","hat"]
        #there are two solutions to this:
        sol 1: we sort each of the words and if the sorted word also matches, then we add to the list
        """
        #creating a defaultdict to store our sorted word as key and the list as value
        count=defaultdict()
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in count:
                count["".join(sorted(strs[i]))].append(strs[i])
            else:
                count["".join(sorted(strs[i]))]=[strs[i]]
        result=[]
        for key,values in count.items():
            result.append(values)
        return result



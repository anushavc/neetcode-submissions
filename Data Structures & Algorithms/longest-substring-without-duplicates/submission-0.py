class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()#keeping track of duplicates
        l=0
        max_length=0
        for r in range(0,len(s)):
            #if we find a duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            #keep traversing until you find duplicate and adding to char set
            charSet.add(s[r])
            max_length=max(max_length,r-l+1)
        return max_length


from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s="racecar"
        r="carrace"
        anagrams, we need to check if they have the same chaarcters and the same amount of each chaarcter
        """
        #check if the length is equal or not
        if len(s)!=len(t):
            return False
        if Counter(s)==Counter(t):
            return True
        else:
            return False

        


        

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s="racecar"
        r="carrace"
        """
        #brute force
        #sorting s
        #sorting t
        if sorted(s)==sorted(t):
            return True
        else:
            return False
            

        
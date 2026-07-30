class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s="racecar"
        r="carrace"
        """
        #hashmap solution
        s_hash={} #hashmap for s
        t_hash={} #hashmap for t
        for i in s:
            if i in s_hash:
                s_hash[i]=s_hash[i]+1
            else:
                s_hash[i]=1
        for i in t:
            if i in t_hash:
                t_hash[i]=t_hash[i]+1
            else:
                t_hash[i]=1
        if s_hash==t_hash:
            return True
        else:
            return False
        


        

        
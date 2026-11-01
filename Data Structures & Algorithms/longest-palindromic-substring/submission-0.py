class Solution:
    def longestPalindrome(self, s: str) -> str:
        #longest_palindrome
        l_p=""
        for i in range(0,len(s)):
            #odd palindrome (center is only character)
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:#finding matching extension
                #if the substring length actually exceeds the current long one, then we set the new substring as longest
                if (r-l+1)>len(l_p):
                    l_p=s[l:r+1]
                l-=1
                r+=1
            #even stage
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:#finding matching extension
                #if the substring length actually exceeds the current long one, then we set the new substring as longest
                if (r-l+1)>len(l_p):
                    l_p=s[l:r+1]
                l-=1
                r+=1
        return l_p
            
                

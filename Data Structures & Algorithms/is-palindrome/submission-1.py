class Solution:
    def isPalindrome(self, s: str) -> bool:
      #palindrome means for a string, the reverse needs to be equal
      #ie;"racecar"="racecar"
      #this question is also relevant to: filtering alphanum and lower case
      #the optimized solution: create alnum function and two pointer solution
      l,r=0,len(s)-1
      while l<r:
        while l<r and not self.alphanum(s[l]):
            l+=1
        while l<r and not self.alphanum(s[r]):
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
        l,r=l+1,r-1
      return True

    def alphanum(self,c):
        return (ord('A')<=ord(c)<=ord("Z") or 
        ord('a')<=ord(c)<=ord('z')or
        ord('0')<=ord(c)<=ord('9')
        )
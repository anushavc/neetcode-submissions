class Solution:
    def isPalindrome(self, s: str) -> bool:
      #palindrome means for a string, the reverse needs to be equal
      #ie;"racecar"="racecar"
      #this question is also relevant to: filtering alphanum and lower case
      newstr=""
      for i in s:
        #check if it is alphanum
        if i.isalnum():
            #add to the new string
            newstr+=i.lower()
      return newstr==newstr[::-1]
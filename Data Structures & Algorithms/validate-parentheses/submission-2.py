class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for i in s:
            #check if it is closing brackets
            if i in pairs:
                if not stack:          # nothing to match with
                    return False
                n = stack.pop()
                if pairs[i] != n:      # wrong match
                    return False
            else:
                stack.append(i)
        return not stack

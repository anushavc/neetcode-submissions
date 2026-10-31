class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={")":"(","]":"[","}":"{"}
        for i in s:
            #if it is opening brackets, then pop into the stack

            #if it is closing brackets, then we match the top of the stack and remove if match or return False
            if i in pairs:
                if stack and stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
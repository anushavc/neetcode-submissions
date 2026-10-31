class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       #logic here is to put them into a stack and when you see an operator, pop out the two characters and the do the "operator" and put the result back into the stack
       stack=[]
       for t in tokens:#checking t is an operator
        if t in "+/*-":
            #popping out
            b=stack.pop()
            a=stack.pop()
            if t=="*":
                stack.append(a*b)
            elif t=="+":
                stack.append(a+b)
            elif t=="/":
                stack.append(int(a/b))
            elif t=="-":
                stack.append(a-b)
        else:
            stack.append(int(t))
       return stack[0]
class MinStack:

    def __init__(self):
        #normal stack
        self.stack=[]
        #stack meant for minimum value storage
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            new_min=min(self.min_stack[-1],val)
        else:
            new_min=val
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

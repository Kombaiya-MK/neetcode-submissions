class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        minValue = value
        if not self.minStack or minValue <= self.minStack[-1]:
            # minValue = self.minStack[-1]
            self.minStack.append(minValue)
        self.stack.append(value)
        

    def pop(self) -> None:
        value= self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        return value
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
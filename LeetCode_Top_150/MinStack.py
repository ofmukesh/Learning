class MinStack:

    def __init__(self):
        self.data=[]
        self.min=[float('inf')]

    def push(self, val: int) -> None:
        self.data.append(val)
        self.min.append(min(self.data[-1],self.min[-1]))

    def pop(self) -> None:
        if len(self.data)>0:
            self.min.pop(-1)
            self.data.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

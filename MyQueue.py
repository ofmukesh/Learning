# this is a queue implement using stack..........
class MyQueue:

    def __init__(self):
        self.s1=[];
        self.s2=[];

    def push(self, x: int) -> None:
        return self.s1.append(x);

    def pop(self) -> int:
        if len(self.s2)>0:
            return self.s2.pop();
        elif len(self.s2)==0 and len(self.s1)>0:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop());
            return self.s2.pop();
        return None;

    def peek(self) -> int:
        if len(self.s2)>0:
            return self.s2[-1];
        elif len(self.s2)==0 and len(self.s1)>0:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop());
            return self.s2[-1];
        return None;

    def empty(self) -> bool:
        return len(self.s1)==0 and len(self.s2)==0;
#................................................

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# This is simple queue using array
class MyQueue:

    def __init__(self):
        self.q=[];

    def push(self, x: int) -> None:
        return self.q.append(x);

    def pop(self) -> int:
        return self.q.pop(0);

    def peek(self) -> int:
        return self.q[0];

    def empty(self) -> bool:
        return len(self.q)==0;


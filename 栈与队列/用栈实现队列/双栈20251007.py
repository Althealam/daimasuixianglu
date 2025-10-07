class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

        

    def push(self, x: int) -> None:
        """push element x to the back of the queue"""
        self.stack_in.append(x)

    def pop(self) -> int:
        """remove the element from the front of the queue and returns it"""
        if len(self.stack_out)!=0:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        """return the element at the front of the queue"""
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

        

    def empty(self) -> bool:
        """return true if the queue is empty"""
        if len(self.stack_in)==0 and len(self.stack_out)==0:
            return True
        return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
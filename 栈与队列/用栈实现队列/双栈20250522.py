class MyQueue:

    def __init__(self):
        # in负责push，out负责pop
        self.stack_in=[]
        self.stack_out=[]
    
    def push(self, x: int) -> None:
        self.stack_in.append(x)
        
    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)): # 将stack_in的元素送到stack_out中，实现先进先出
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int:
        ans=self.pop()
        self.stack_out.append(ans)
        return ans
        

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.main_stack = [] # 主栈
        self.min_stack = [] # 辅助栈
        

    def push(self, val: int) -> None:
        """将元素val推入栈中"""
        self.main_stack.append(val)
        if len(self.min_stack)==0 or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        """删除堆栈顶部的元素"""
        if self.main_stack.pop()==self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        """获取堆栈顶部的元素"""
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        """获取堆栈中的最小元素"""
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
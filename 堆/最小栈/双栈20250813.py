# 时间复杂度：O(1)
# 空间复杂度：O(N) 当共有N个待入栈元素时，辅助栈B最差情况下存储N个元素
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        初始化堆栈对象
        """
        self.A = [] # 存储所有元素
        self.B = [] # 存储A中非严格降序元素的子序列（因此B的栈顶元素是最小值）
        

    def push(self, x: int) -> None:
        """将元素x推入堆栈"""
        self.A.append(x) # 不管顺序如何，A中都加入元素，但是B只存储小元素
        if not self.B or self.B[-1]>=x: # x比B的栈顶元素小，因此加入栈中
            self.B.append(x)
        

    def pop(self) -> None:
        """删除堆栈顶部的元素"""
        if self.A.pop()==self.B[-1]: 
            self.B.pop()
        

    def top(self) -> int:
        """获取堆栈顶部的元素"""
        return self.A[-1]
        

    def getMin(self) -> int:
        """获取堆栈中的最小元素"""
        return self.B[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
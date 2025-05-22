# 思路：用两个队列来模拟，其中另外一个队列是用来存储元素的
class MyStack:

    def __init__(self):
        self.queue_in=deque()
        self.queue_out=deque()
        

    def push(self, x: int) -> None:
        # 元素x入栈
        self.queue_in.append(x)

    def pop(self) -> int:
        # 移除栈顶元素
        # 将queue_in的所有元素（除了最后一个），依次出列放进queue_out
        # 交换in和out，此时out里只有一个元素
        # 把out中的pop出来，即是原队列的最后一个
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()
   

    def top(self) -> int:
        # 获取栈顶元素
        # 1. 将queue_in中的所有元素（除了最后一个）依次出列放进queue_out
        # 2. 交换in和out，此时out中只有一个元素
        # 3. 将out中的pop出来，即是原队列中的最后一个，使用temp变量暂存
        # 4. 把temp追加到queue_in的末尾
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        temp=self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp
        

    def empty(self) -> bool:
        # 返回栈是否为空
        return len(self.queue_in)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
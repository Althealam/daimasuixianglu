# 队列：先进先出 
# 栈：先进后出
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        in：存所有数据
        out：仅仅在pop的时候会用到
        """
        self.queue_in=deque()
        self.queue_out=deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_in.append(x)
        

    def pop(self):
        """
        :rtype: int
        1. 检查队列是否为空
        2. 不为空的话，将需要弹出的元素之前（包括需要弹出的元素）的元素入队列
        3. 将queue_in中需要弹出的元素之前的元素出队，放到queue_out中
        4. 交换queue_in和queue_out
        5. 弹出queue_out中的元素
        """
        if self.empty():
            return None
        
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out=self.queue_out, self.queue_in
        return self.queue_out.popleft()
        

        

    def top(self):
        """
        :rtype: int
        1. 确认不为空
        2. 先将queue_in中的所有元素（除了最后一个）依次出列放到queue_out中
        3. 交换in和out，现在out中只有一个元素
        4. 把out中的一个元素pop出来，即是队列的最后一个，用temp暂存
        5. 把temp追加到queue_in的末尾
        """
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out=self.queue_out, self.queue_in
        temp=self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue_in)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
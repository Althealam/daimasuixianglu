# push：元素x入栈
# pop：移除栈顶元素
# top：获取栈顶元素
# empty：返回栈是否为空
# 思路：队列是先进先出的，把一个队列的数据导入另一个队列中，数据的顺序并没有变，并没有变成先进后出的顺序
# 用队列模拟栈，只要用一个队列就可以了
# 出元素时，只要让出队列的元素再加入回队列里，就可以模拟栈了
# 假设队列里有size个元素，弹出size-1个元素，并且将这些元素重新加入队列
class MyStack(object):

    def __init__(self):
        """
        in：存所有数据
        out：仅在pop的时候会用到
        """
        self.queue_in=deque()
        self.queue_out=deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        直接append即可
        """
        self.queue_in.append(x)


    def pop(self):
        """
        :rtype: int
        1. 首先确认不空
        2. 由于队列的特殊性，所以我们只有在pop的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
        """
        if self.empty():
            return None
        
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in,self.queue_out=self.queue_out,self.queue_in # 交换in和out
        return self.queue_out.popleft()


    def top(self):
        """
        :rtype: int
        方法一：
        1. 确认不空
        2. 我们仅有in会存储数据，所以返回第一个即可
        方法二：
        1. 确认不空
        2. 由于队列的特殊性，因此我们只有在pop的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有最后一个元素
        5. 把out中的pop出来，即是原队列的最后一个，并且使用temp变量暂时存放
        6. 把temp追加到queue_in的末尾
        """
        # 方法一
        # if self.empty():
        #     return None
        # return self.queue_in[-1]

        # 方法二
        if self.empty():
            return None

        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out=self.queue_out,self.queue_in
        temp=self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp



    def empty(self):
        """
        :rtype: bool
        只有in存储了数据，只要判断in是不是有数即可
        """
        return len(self.queue_in)==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
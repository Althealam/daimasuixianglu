class MyQueue(object):

    def __init__(self):
        """
        stack_in负责push，stack_out负责out
        队列是先进先出，栈是后进先出
        """
        self.stack_in=[]
        self.stack_out=[]
        

    def push(self, x):
        """
        将一个元素放入队列的尾部
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x) # 先进去的元素就会在队列的尾部
        

    def pop(self):
        """
        从队列首部移除元素
        :rtype: int
        """
        if self.empty():
            return None
        if self.stack_out: # 如果stack_out不为空，说明有元素被转移到这个栈中等待出队了，移除这个栈的栈顶元素，就相当于移除了队列头部的元素
            return self.stack_out.pop() 
        else:
            # stack_out为空，则将stack_in中的元素移动到stack_out中，从而实现移除队列首部的元素
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

        

    def peek(self):
        """
        返回队列首部的元素
        :rtype: int
        """
        ans=self.pop()
        self.stack_out.append(ans)
        return ans
        

    def empty(self):
        """
        返回队列是否为空
        :rtype: bool
        """
        return not (self.stack_in or self.stack_out)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
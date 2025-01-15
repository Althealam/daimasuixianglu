class Stack:
    def __init__(self):
        self.array = []  # 存储栈元素的列表
        self.size = 0    # 栈的大小
        self.top = -1   # 栈顶指针，初始为 -1，表示栈为空

    def is_empty(self):
        """
        判断栈是否为空
        :return: True 如果栈为空，False 否则
        """
        return self.size == 0

    def push(self, value):
        """
        入栈操作
        :param value: 要入栈的值
        """
        # 移动栈顶指针
        self.top += 1
        # 如果栈的大小小于等于栈顶指针，说明需要扩容
        if self.size <= self.top:
            self.array.append(value)
            self.size += 1
        else:
            # 直接更新栈顶元素的值
            self.array[self.top] = value

    def pop(self):
        """
        出栈操作
        :return: 出栈的元素，如果栈为空返回 None
        """
        if self.is_empty():
            return None
        value = self.array[self.top]
        self.top -= 1
        return value

    def peek(self):
        """
        查看栈顶元素
        :return: 栈顶元素，如果栈为空返回 None
        """
        if self.is_empty():
            return None
        return self.array[self.top]


# 测试代码
stack = Stack()
print("初始栈是否为空:", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("入栈 1, 2, 3 后栈顶元素:", stack.peek())
print("出栈元素:", stack.pop())
print("出栈元素:", stack.pop())
print("出栈元素:", stack.pop())
print("出栈元素:", stack.pop())  # 尝试从空栈出栈
print("最终栈是否为空:", stack.is_empty())
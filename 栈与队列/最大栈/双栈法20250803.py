# 设计一个最大栈数据结构，支持以下操作：
# 1. push(x)：将元素x压入栈中
# 2. pop()：移除栈顶元素并返回该元素
# 3. top()：返回栈顶元素（不移除）
# 4. getMax()：返回栈中当前的最大元素

# 思路：双栈法
# 1. 使用两个栈：主栈（存储所有元素），辅助栈（存储当前的最大元素）
# 2. push(x)：主栈压入x，辅助栈压入max(x, 辅助栈顶元素) 如果辅助栈为空则直接压入严肃
# 3. pop()：两个栈同时弹出栈顶元素
# 4. top(), getMax()：直接返回主栈顶和辅助栈顶元素

class MaxStack:
    def __init__(self):
        self.main_stack = [] # 主栈
        self.max_stack = [] # 辅助栈
    
    def push(self, x):
        self.main_stack.append(x)
        if len(self.max_stack)==0:
            self.max_stack.append(x)
        else:
            current_max = max(x, self.max_stack[-1])
            self.max_stack.append(current_max)
    
    def pop(self):
        if len(self.max_stack)==0:
            return None
        self.max_stack.pop()
        return self.main_stack.pop()

    def top(self):
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def getMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

max_stack = MaxStack()
max_stack.push(5)
max_stack.push(1)
max_stack.push(5)

print(max_stack.top())
print(max_stack.getMax())

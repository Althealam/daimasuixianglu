import heapq
class MaxStack:
    def __init__(self):
        self.stack = [] # 存储栈元素的列表，每个元素为【值，索引】的形式
        self.heap = [] # 最小堆
        self.removed = set() # 集合，用于标记已经删除但是尚未从数据结构中清理的元素索引
        self.idx = 0 # 自增索引，用于唯一标识每个入栈元素
    
    def push(self, x):
        """将元素x压入栈中"""
        self.stack.append([x, self.idx])
        heapq.heappush(self.heap, [-x, -self.idx]) # 将其压入堆中，通过负值实现最大堆的效果
        self.idx+=1
    
    def pop(self):
        """移除栈顶元素并返回这个元素"""
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, i = self.stack.pop() # 弹出栈顶元素，并记录其索引
        self.removed.add(i) # 在移除的set中加入索引
        return num
    
    def top(self):
        """返回栈顶元素并且不需要移除"""
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self):
        """检索并返回栈中的最大元素，不需要移除"""
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]
    
    def popMax(self):
        """检索并返回栈中的最大元素，需要移除"""
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        # 弹出堆顶元素，记录其索引到removed集合中
        num, i = heapq.heappop(self.heap) 
        self.removed.add(-1)
        return -i

ms = MaxStack()
ms.push(5)
ms.push(1)
ms.push(5)



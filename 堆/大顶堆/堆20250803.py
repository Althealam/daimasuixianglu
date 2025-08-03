import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        """插入负值，使小顶堆的行为模拟大顶堆"""
        heapq.heappush(self.heap, -val)
    
    def pop(self):
        """移除并返回堆顶元素（最大值）"""
        return -heapq.heappop(self.heap)

    def peek(self):
        """返回堆顶元素（最大值）但是不移除"""
        return -self.heap[0]

    def size(self):
        """返回堆中元素的数量"""
        return len(self.heap)

    def is_empty(self):
        """判断堆是否为空"""
        return self.size()==0
    
max_heap = MaxHeap()
max_heap.push(3)
max_heap.push(1)
max_heap.push(5)
max_heap.push(2)

print(f"堆大小: {max_heap.size()}")  # 输出: 4
print(f"堆顶元素: {max_heap.peek()}")  # 输出: 5

# 弹出元素
print(f"弹出元素: {max_heap.pop()}")  # 输出: 5
print(f"新堆顶元素: {max_heap.peek()}")  # 输出: 3

# 继续弹出
print(f"弹出元素: {max_heap.pop()}")  # 输出: 3
print(f"弹出元素: {max_heap.pop()}")  # 输出: 2
print(f"弹出元素: {max_heap.pop()}")  # 输出: 1
print(f"堆是否为空: {max_heap.is_empty()}")  # 输出: True
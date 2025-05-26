# 大顶堆的构造过程：
# 1. 先将n个元素的无序排序，构造成大顶堆（弄成一个二叉树）
# 2. 将根节点与最后一个节点交换位置（将最大元素沉到数组末端）
# 3. 交换过后可能不再满足大顶堆的条件，所以需要将剩下的n-1个元素重新构造成一个大顶堆
# 4. 重复2.3步骤，直到整个数组排序完成
# 总结：每次都判断根节点与当前遍历节点的大小，将较大的元素沉到数组的末端

class MaxHeap:
    def __init__(self, capacity=10):
        """初始化大顶堆"""
        self.heap=[0]*capacity
        self.size=0
        self.capacity=capacity
    
    def _parent(self, index):
        """返回父节点的索引"""
        return (index-1)//2
    
    def _left_child(self, index):
        """返回左子节点的索引"""
        return 2*index+1

    def _right_child(self, index):
        """返回右子节点的索引"""
        return 2*index+2

    def _swap(self, i, j):
        """交换两个节点的值"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """向上调整堆，让大的元素下沉到数组末端"""
        while index>0 and self.heap[index]>self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index=self._parent(index)
    
    def _heapify_down(self, index):
        """向下调整堆，让最小的元素下沉到数组末端"""
        largest=index
        left=self._left_child(index)
        right=self._right_child(index)
        if left<self.size and self.heap[left]>self.heap[largest]:
            largest=left
        if right<self.size and self.heap[right]>self.heap[largest]:
            largest=right

        if largest!=index:
            self._swap(index, largest)
            self._heapify_down(largest)
    
    def insert(self, value):
        """插入元素到堆中"""
        if self.size>=self.capacity:
            # 扩展堆容量
            self.heap=self.heap+[0]*self.capacity
            self.capacity*=2
        
        self.heap[self.size]=value
        self.size+=1
        self._heapify_up(self.size-1)

    def extract_max(self):
        """移除并返回最大值"""
        if self.size==0:
            return None

        max_value=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self._heapify_down(0)
        return max_value
    
    def get_max(self):
        """返回最大值但是不移除"""
        if self.size==0:
            return None
        return self.heap[0]
    
    def is_empty(self):
        """判断堆是否为空"""
        return self.size==0
    
    def build_heap(self, arr):
        """从数组构建堆"""
        self.heap=arr.copy()
        self.size=len(arr)
        self.capacity=len(arr)
        # 从最后一个非叶子节点开始向下调整
        for i in range(self.size//2-1, -1, -1):
            self._heapify_down(i)
    
    def heap_sort(self):
        """堆排序"""
        sorted_arr=[]

        while self.size>0:
            sorted_arr.append(self.extract_max())
        
        # 恢复到堆的原始状态
        self.build_heap(sorted_arr[::-1])
        return sorted_arr[::-1] # 反转得到升序

if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    heap.insert(10)
    heap.insert(8)
    
    print("堆的最大值:", heap.get_max())  # 输出: 10
    print("提取最大值:", heap.extract_max())  # 输出: 10
    print("堆排序结果:", heap.heap_sort())  # 输出: [1, 3, 5, 8]
    
    # 从数组构建堆
    arr = [4, 1, 7, 3, 9, 2]
    heap.build_heap(arr)
    print("从数组构建的堆排序结果:", heap.heap_sort())  # 输出: [1, 2, 3, 4, 7, 9] 
# 双堆解法（普通解法的时候需要先将元素排序然后直接取中间值，这样的话时间复杂度为O(nlogn)）
# 时间复杂度：
# 1. 查找中位数：O(1)
# 2. 添加数字：O(logn)
# 空间复杂度：O(n) 其中n为数据流中的元素数量

# 思路：建立一个小顶堆和大顶堆，各自保存列表的一半元素，并且规定
# 1. A保存较大的一半，长度为N/2或者N+1/2，假设有m个元素
# 2. B保存较小的一半，长度为N/2或者N+1/2，假设有n个元素
# 随后，中位数可以根据A和B的堆顶元素得到
# 如果m!=n，那么N为奇数，也就是说中位数在小顶堆中
# 如果m=n，那么N为偶数，也就是说中位数是小顶堆和大顶堆的堆顶元素的一半

# 分析：假设现在有元素[1,3,5,7,9]，中位数是5，此时新增加元素6
# A：[5,7,9] B：[-3, -1]
# 增加6后，需要让A和B各自存储3个元素
# 先将6加入到A中，再弹出A的堆顶5到B中
# 最终A是[6,7,9]，B是[-5,-3,-1]
# 那么中位数是(6+5)/2=5.5
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半
    
    def addNum(self, num):
        """注意需要平衡两个堆，让两个堆的长度差不超过1"""
        if len(self.A)!=len(self.B):
            # N为奇数：将新元素num加入到A中，再将A堆顶元素插入到B中
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A)) # 这里加入负数是因为希望通过小顶堆来实现大顶堆，因为heapq实现的是小顶堆
        else:
            # N为偶数：将新元素num加入到B中，再将B堆顶元素插入到A中
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
    
    def findMedian(self):
        # 当m=n的时候中位数为A的堆顶元素+B的堆顶元素//2
        # 当m!=n的时候中位数为A的堆顶元素
        return self.A[0] if len(self.A)!=len(self.B) else (self.A[0]-self.B[0])/2
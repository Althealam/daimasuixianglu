# 思路：每次滑动窗口时push进去元素，移动滑动窗口时pop掉不需要的元素
# 实现自定义单调队列，确保最大元素一直在单调队列的出口处（维护最大值）
# 设计单调队列时，pop和push操作保持如下规则：
# pop(value)：如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
# push(value)：如果push的元素value大于入口元素的数值，那么就将队列入口的元素弹出，直到push元素的数值小于等于队列入口的数值为止

# 时间复杂度：O(nk)，其中n是数组的长度，k是一个滑动窗口内比较的元素个数
# 空间复杂度：O(n)

from collections import deque

class MyQueue: # 单调队列，从大到小
    def __init__(self):
        self.queue=deque() # 使用deque实现单调队列，使用list会超时

        # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值
        # 通过pop之前要判断队列是否为空
    def pop(self,value):
        if self.queue and value==self.queue[0]:
            self.queue.popleft()
            # list.pop()的时间复杂度为O(n)

        # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值
    def push(self,value):
        while self.queue and value>self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

        # 查询当前队列的最大值，直接返回队列前端也就是front即可
    def front(self):
        return self.queue[0]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que=MyQueue()
        result=[]
        for i in range(k): # 先将前面k个元素放进队列
            que.push(nums[i])
        result.append(que.front()) # result记录前k个元素的最大值
        for i in range(k,len(nums)):
            que.pop(nums[i-k]) # 滑动窗口移除最前面元素
            que.push(nums[i]) # 滑动窗口前加入最后面的元素
            result.append(que.front()) # 记录对应的最大值
        return result
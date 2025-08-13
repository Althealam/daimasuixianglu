class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*(len(nums)-k+1) # 答案数量为len(nums)-k+1
        q = deque() # 双端队列
        for i, x in enumerate(nums):
            # 1. 右边入
            while q and nums[q[-1]]<=x: # 遇到了比队首元素更大的元素
                q.pop() # 维护双端队列的单调性
            q.append(i)

            # 2. 左边出
            left = i-k+1 # 窗口左端点
            if q[0]<left:
                q.popleft()
            
            # 3. 在窗口左端点记录答案值
            if left>=0:
                ans[left] = nums[q[0]] # 队首元素就是最大值
        return ans 
        
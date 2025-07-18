# 思路：双端队列，右边入左边出，设置双端队列为单调递增的
# 1. 如果当前遍历的元素值大于队首元素，则弹出队首元素，加入当前元素
# 2. 如果当前已经离开了窗口，则弹出左边的元素
# 3. 窗口的最大值就在队首，记录队首元素

# 通过双端队列 找到每个滑动窗口的最大值 然后滑动窗口的最大值就是队首元素 每次记录队首元素即可
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*(len(nums)-k+1)  # 窗口的个数
        # 对于长度为len(nums)的数组，如果要其滑动窗口大小为k，那么滑动窗口总共有len(nums)-k+1个
        q = deque()
        for i in range(len(nums)):
            # 还在滑动窗口内，并且当前遇到的元素比队尾元素要大
            while q and nums[i]>=nums[q[-1]]: 
                q.pop()
            q.append(i)
        
            # 队首已经离开了滑动窗口
            left = i-k+1 # 这是此时的滑动窗口的最左端
            if q[0]<left: # 队首元素已经离开了滑动窗口，则弹出最左边的元素
                q.popleft()
            
            if left>=0: # 此时还在滑动窗口内
                ans[left]=nums[q[0]] # 队首元素就是当前滑动窗口内的最大值
        
        return ans
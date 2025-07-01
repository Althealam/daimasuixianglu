# 思路：堆化->除去前k-1个最大元素->得到第k个最大元素
# 堆其实是一个完全二叉树，在存储结构上是线性数组

# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def shiftdown(nums, i, n):
            while 2*i+1<n:
                j = 2*i+1
                if j+1<n and nums[j+1]>nums[j]:
                    j+=1
                if nums[i]>=nums[j]:
                    break
                nums[j], nums[i] = nums[i], nums[j]
                i = j
        
        # Heapify
        n = len(nums)
        for i in range(int((n-1)/2), -1, -1):
            shiftdown(nums, i, n)
        
        # 删除前面的K-1个最大值
        for _ in range(k-1):
            nums[n-1], nums[0] = nums[0], nums[n-1]
            n-=1
            shiftdown(nums, 0, n)
        
        # 选择第K大元素
        return nums[0]
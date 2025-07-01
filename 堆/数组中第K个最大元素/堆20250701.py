# 思路：堆化->除去前k-1个最大元素->得到第k个最大元素
# 堆其实是一个完全二叉树，在存储结构上是线性数组

# 时间复杂度：O(n+klogn)
# （1）堆化：对于每个节点i，shiftdown的时间复杂度为O(logn)（树高为logn)，并且节点数量为n，因此总的为nlogn
# （2）移除k-1个元素：O(klogn)，总共循环k-1次，每次调整堆顶元素的时间为O(logn)

# 空间复杂度：
# （1）递归：O(logn)
# （2）迭代：O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def shiftdown(nums, i, n):
            """堆化，确保父节点的值大于子节点，如果不满足的话则交换父节点和较大子节点的值"""
            largest = i
            left = 2*i+1
            right = 2*i+2

            if left<n and nums[left]>nums[largest]:
                largest = left

            if right<n and nums[right]>nums[largest]:
                largest = right
            
            if largest!=i:
                nums[i], nums[largest] = nums[largest], nums[i]
                shiftdown(nums, largest, n)
        
        # Heapify
        # 从最后一个节点开始调整，构造最大堆
        n = len(nums)
        for i in range(n//2-1, -1, -1): # 最后一个非叶子节点的下标是n//2-1
            shiftdown(nums, i, n)
        
        # 删除前面的K-1个最大值
        for _ in range(k-1):
            nums[n-1], nums[0] = nums[0], nums[n-1] # 每次都将堆顶元素（最大值）和堆的最后一个元素交换
            n-=1 # 堆的大小减去1
            shiftdown(nums, 0, n) # 重新调整堆，确保新的堆顶是剩余元素中最大的
        
        # 选择第K大元素
        return nums[0]
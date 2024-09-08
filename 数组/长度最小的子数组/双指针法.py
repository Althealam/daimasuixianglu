# 方法二：双指针法（滑动窗口法）
# 窗口就是满足其和>=s的长度最小的连续子数组
# 窗口的结束位置就是遍历数组的指针，也就是for循环里的索引
# 时间复杂度：O(n)，n是数组nums的长度
# 分析：双指针法只遍历数组一次，右指针right从左到右遍历整个数组，左指针left可能会随着窗口的缩小而移动，但是每个元素最多被访问两次（一次由右指针增加，一次由左指针减少）
# 空间复杂度：O(1)
# 分析：双指针法使用固定数量的额外空间，即几个指针变量

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0 # 左指针
        right=0 # 右指针
        min_len=float('inf') # 初始化最小长度为无穷大
        cur_sum=0 # 当前的累加值

        for right in range(n): # 右指针从0到n-1
            cur_sum+=nums[right] # 将右指针的值加到当前和
            # 当当前和大于等于target时，尝试缩小窗口
            while cur_sum>=target: # 当前累加值大于目标值
                min_len=min(min_len,right-left+1) # 更新最小长度
                cur_sum-=nums[left] # 从当前和减去左指针的值
                left+=1 # 移动左指针，缩小窗口
        
        return min_len if min_len!=float('inf') else 0
# 方法：贪心法
# 思路：
# 1. 初始化变量：result用于存储迄今为止找到的最大子数组和；count用于追踪当前子数组的和
# 2. 遍历数组：将当前元素nums[i]加到count中，以更新当前子数组和；判断count是否比result大，如果count>result，就更新result
# 3. 判断是否重置count：如果count<=0，我们将count重置为0（count为负数的时候，继续加上后面的元素只会降低子数组的和）

# 时间复杂度：利用for循环遍历整个数组nums，并且在每个循环中，只进行了一些常数时间的加法、条件判断和赋值操作
# 总的时间复杂度为O(n)
# 空间复杂度：只使用了常数个额外的变量：result和count，用来存储当前的最大和和当前子数组对的和
# 总的空间复杂度为O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=float('-inf') # 初始化结果为负无穷大
        count=0 
        for i in range(len(nums)):
            count+=nums[i]
            if count>result: # 取区间累计的最大值
                result=count
            if count<=0: # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                count=0
        return result
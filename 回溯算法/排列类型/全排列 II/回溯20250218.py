# 1. 递归函数的参数和返回值：result, path , nums
# 2. 终止条件：len(path)==len(nums)
# 3. 单层搜索的逻辑
# 树层去重：if used[i]: continue
# if i>0 and nums[i]==nums[i-1] and used[i-1]: continue

# 时间复杂度：O(n*n!)
# 1. 全排列的生成：对于一个长度为n的数组，全排列的总数为n!个
# 2. 单层搜索的逻辑：backtracking有一个for遍历nums中的所有元素，最坏情况下每次调用的时候for循环都要使用n次
# 空间复杂度：O(n*n!)
# 1. 递归调用栈的深度：最大为n
# 2. 辅助数组used的空间：n
# 3. 结果列表的空间：全排列的总数为n!，每个排列的长度为n


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        used=[False]*len(nums)
        self.backtracking(result, [], used, nums)
        return result
    
    def backtracking(self, result, path, used, nums):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1] and used[i-1]) or used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(result, path, used, nums)
            path.pop()
            used[i]=False

        
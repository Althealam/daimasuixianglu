# 1. 递归函数的参数和返回值：path, result, startIndex, nums
# 2. 终止条件：if len(path)==len(nums): result.append(path[:])
# 3. 单层搜索的逻辑
# 剪枝：树枝上去重（前提是这个nums是没有重复元素的）：if nums[i] in path: return 

# 时间复杂度：O(n*n!)
# 1. 全排列的数量：对于一个长度为n的数组，它的全排列的数量是n!（第一个位置有n个选择，第二个位置有n-1个选择，最后一个位置有1个选择）
# 2. 生成每个全排列的开销：path[:]的时间复杂度为O(n)
# 3. 检查元素是否已经在路径中的开销：O(n)

# 空间复杂度：O(n*n!)
# 1. 递归调用栈的深度：数组的长度n
# 2. 存储结果需要的空间：数组个数最多为n!，每个数组的长度最多为n
# 3. 存储当前路径需要的空间：path需要存储当前路径，O(n)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backtracking([],result, 0, nums)
        return result
    
    def backtracking(self, path, result, startIndex, nums):
        if len(path)==len(nums):
            result.append(path[:])
            return 
        for i in range(0, len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i]) # 树枝上去重
            self.backtracking(path, result, i, nums)
            path.pop()
        
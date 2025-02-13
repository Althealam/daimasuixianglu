# 1. 递归函数的参数和返回值：path, result, nums, startIndex
# 2. 终止条件：其实没有终止条件，每次递归的时候都result.append(path[:])
# 3. 单层搜索的逻辑和之前组合的类似

# 时间复杂度：O(2^n*n)
# 1. 子集数量：2^n（对于一个长度为n的数组，数组中的每个元素都有2个选择，因此是2^n个选择）
# 2. 生成每个子集的操作：path[:]是一个复制操作，O(n)

# 空间复杂度：O(2^n*n)
# 1. 递归调用栈的深度：栈的最大深度为n，O(n)
# 2. 存储结果需要的空间：子集数量为2^n，每个子集的最大长度为n，O(2^n*n)
# 3. 存储临时子集的空间：path来存储当前正在生成的子集，O(n)（path的最大长度为n）
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backtracking(result, [], nums, 0)
        return result
    
    def backtracking(self, result, path, nums, startIndex):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(result, path, nums, i+1)
            path.pop()

        
        
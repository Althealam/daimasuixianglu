# 1. 递归函数的参数和返回值：result, nums, path, startIndex
# 2. 终止条件：没有，每一层都需要收割（除了数组长度小于2的）
# 3. 单层搜索的逻辑
# 剪枝：
# （1）剪去nums[i]小于数组的最后一个元素的：if path and nums[i]<path[-1]: continue
# （2）剪去nums[i]在当前层使用过的（当前树枝使用过的没关系）：if nums[i] in used: continue
# （3）剪去path的长度小于2的：if len(path)>=2: result.append(path[:])


# 时间复杂度：O(2^n*n)
# 1. 子序列的数量上限：2^n（对于每个数组的元素都有两种可能）
# 2. 每次生成子序列的开销：path[:]为O(k)，并且k最大为n
# 3. 剪枝操作：O(1)
# 空间复杂度：O(2^n*n)
# 1. 递归调用栈的深度：数组的长度n，O(n)
# 2. 存储结果需要的空间：最多有2^n个数组，每个数组的最大长度为n，O(2^n*n)
# 3. 辅助空间：used存储使用过的元素，O(n)

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backtracking([],result, nums, 0)
        return result
    
    def backtracking(self, path, result, nums, startIndex):
        if len(path)>=2:
            result.append(path[:])
        used=set() # 存储当前层已经使用过的元素（避免出现重复元素）
        for i in range(startIndex, len(nums)): # 相当于一个树枝（startIndex的变化相当于一个树层）
            if path and nums[i]<path[-1]: # 剪去不是递增的数组（确保新增的元素是大于数组的最后一个元素的）
                continue 
            if nums[i] in used: # 剪去用过的元素（重复元素）
                continue
            used.add(nums[i])
            path.append(nums[i])
            self.backtracking(path, result, nums, i+1)
            path.pop()
        
        
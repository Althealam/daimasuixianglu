# 剪枝：
# （1）剪去nums[i]小于path的最后一个元素的
# （2）剪去nums[i]在当前层已经使用过的
# （3）剪去path的长度小于2的

# 时间复杂度：O(2^n*n)
# 1. 子序列的数量上限：2^n（每个数组的元素都有两种可能）
# 2. 每次生成子序列的开销：path[:]为O(k)，并且k最大为n
# 3. 剪枝操作：O(1)

# 空间复杂度：
# 1. 递归调用栈的深度：数组的长度为n，O(n)
# 2. 存储结果需要的空间：最多有2^n个数组，每个数组的长度最大为n，O(2^n*n)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, nums, 0)
        return result
    
    def traversal(self, result, path, nums, startIndex):
        if len(path)>=2 and path not in result:
            result.append(path[:])
        for i in range(startIndex, len(nums)):
            if path and nums[i]<path[-1]:
                continue
            path.append(nums[i])
            self.traversal(result, path, nums, i+1)
            path.pop()
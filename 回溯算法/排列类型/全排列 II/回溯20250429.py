# 时间复杂度：O(n*n!)
# 1. 全排列的生成：对于一个长度为n的数组，全排列的总数为n!个
# 2. 单层搜索的逻辑：回溯有一个for循环遍历nums中的所有元素，最坏情况下每次调用的时候for循环都要使用n次
# 空间复杂度：O(n*n!)
# 1. 递归调用栈的深度：最大为n
# 2. 辅助数组used的空间：n
# 3. 结果列表的空间：全排列的总数为n!，每个排列的长度为n

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        nums.sort()
        used=[False]*len(nums)
        self.traversal(result, path, nums, used)
        return result
    
    def traversal(self, result, path, nums, used):
        if len(path)==len(nums) and path not in result:
            result.append(path[:])
            return 
        for i in range(len(nums)):
            if used[i]: # nums[i]已经被使用过了
                continue
            if i>0 and nums[i]==nums[i-1] and used[i-1]: # 剪去相同的枝
                continue
            path.append(nums[i])
            used[i]=True
            self.traversal(result, path, nums, used)
            path.pop()
            used[i]=False
        
# 1. 递归函数的参数和返回值：path, result, nums, startIndex
# 2. 终止条件：没有终止条件，每个节点都要收获一次结果
# 3. 单层搜索的逻辑：
# 注意需要剪枝，这里的剪枝指的是剪去数组相同得到枝
# （1）return：递归函数的剩余代码不再执行，直接返回到上一层递归
# （2）continue：跳过当前循环体的剩余代码，直接开始下一次迭代循环

# 时间复杂度：O(n*2^n)
# 1. 排序：O(nlogn)
# 2. 回溯：对于一个长度为n的数组，子集的数量为2^n。对于每个子集，都要复制子集放到结果集中，path[:]的时间复杂度为O(k)
# 因此回溯的时间复杂度为O(n*2^n)

# 空间复杂度：O(n*2^n)
# 1. 递归调用栈的深度：数组的长度n（树的最大深度为n）
# 2. 存储结果需要的空间：O(n*2^n)（每个数组最大长度为n，最多要存储2^n个数组）
# 3. 存储临时子集：path为O(n)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        self.backtracking([],result, nums, 0)
        return result
    
    def backtracking(self, path, result, nums, startIndex):
        result.append(path[:])

        for i in range(startIndex, len(nums)):
            # i>startIndex确保当前元素不是该层递归的第一个元素，并且和前一个元素相同，才跳过该元素
            if i>startIndex and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(path, result, nums, i+1)
            path.pop() # 撤销上一步，将当前元素从path中移除
        
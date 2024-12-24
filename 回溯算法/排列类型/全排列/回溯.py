# 分析：排列是强调元素顺序的，比如[2,1]和[1,2]是两个不同的排列
# 之前的startIndex是为了避免出现[1,2]和[2,1]的情况的
# 1. 递归函数参数：used数组用来标记已经选择的元素
# 2. 递归终止条件：叶子结点就是收割结果的地方
# 达到叶子结点：path的大小和nums数组一样大的时候，说明找到了一个全排列，也就是达到了叶子结点
# 3. 单层搜索的逻辑
# 与之前的子集问题、组合问题的区别：
# 1. 每层都是从0开始而不是startIndex
# 2. 需要used数组记录path里都放了哪些元素了
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        path=[]
        used=[False]*len(nums)
        self.backstracking(nums,path,used,result)
        return result
    
    def backstracking(self,nums,path,used,result):
        # 收集结果的条件->到达叶子结点->当path的长度和nums相同
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)): # 树层（横向扩展）
        # 在当前层次中，遍历nums中的每一个元素，尝试将它们添加到path中
            # 树层去重
            if used[i]:
                continue
            # 设置used[i]
            used[i]=True
            path.append(nums[i])
            self.backstracking(nums,path,used,result) # 树枝（纵向扩展）
            # 回溯
            path.pop()
            used[i]=False
        
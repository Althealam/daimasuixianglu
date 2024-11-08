# 方法：回溯法（未使用剪枝）
# 分析：与之前题目不同的是，树的深度由target来决定了，也就是树的深度并不是固定的
# 1. 确定函数的参数和返回值：全局变量：二维数组result（结果集）、一维数组path（路径数组）
# 2. 确定终止条件
# 3. 确定单层递归逻辑


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backstracking(candidates,target,0,0,[],result)
        return result

    def backstracking(self,candidates,target,sum,startIndex,path,result):
        # startIndex的作用和之前的题目一样，是用来避免收集重复的结果的
        # 终止条件
        if sum>target:
            return
        if sum==target:
            result.append(path[:])
            return
        # 单层搜索的逻辑
        for i in range(startIndex,len(candidates)):
            # 这里为什么不是len(candidates)+1?
            path.append(candidates[i])
            sum+=candidates[i]
            # 由于元素是可以重复使用的，所以startIndex和之前不一样，这里是i，而不是i+1
            self.backstracking(candidates,target,sum,i,path,result)
            # 回溯
            path.pop()
            sum-=candidates[i]

        


        
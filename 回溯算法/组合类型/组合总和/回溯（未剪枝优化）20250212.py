# 1. 递归函数的参数和返回值：path路径，result结果集，target目标和，startIndex下次开始的位置
# 2. 终止条件：
# （1）if sum(path)==target: result.append(path[:]) return
# （2）if sum(path)>target: return （注意这里需要直接return，否则一棵树的边会一直递归下去），这里也是剪枝的操作
# 3. 单层递归的逻辑：
# path.append(candidates[i]) self.backtracking(...) path.pop()

# 时间复杂度：
# 假设candidates的长度为n，数组中最小元素值为min，目标值为target，那么树的最大深度为target/min


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backtracking([],result, target, candidates, 0)
        return result
    
    def backtracking(self, path, result, target, candidates, startIndex):
        # if sum(path)>target:
        #     return 
        if sum(path)==target:
            result.append(path[:])
            return 
        for i in range(startIndex, len(candidates)):
            # 这里一定是range(startIndex, len(candidates))而不是range(0, len(candidates))
            # 否则会出现[2,2,3], [2,3,2]这两种数组同时出现的情况
            if sum(path)<target: # 剪枝
                path.append(candidates[i])
                self.backtracking(path, result, target, candidates, i) # 可以不用i+1，表示可以重复读前面的数
                path.pop()
                

        
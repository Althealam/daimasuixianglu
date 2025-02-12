# 1. 递归函数的参数和返回值：result, path, target, candiates, startIndex
# 2. 终止条件：sum(path)==target: result.append(path[:]) return
# 3. 单层递归的逻辑：
# （1）利用candidates[i]==candidates[i-1]进行剪枝
# （2）利用sum(path)>target进行剪枝
# （3）在path中加入candidates[i]，并且下次递归从i+1开始，表示不能重复选择数字


# 时间复杂度：
# 1. 对于每个数字都有选或者不选两个情况，可能的组合数是2^n
# 2. 每次搜索都有复制操作，时间复杂度为k，k最大情况下为n
# 3. 排序的时间复杂度为O(nlogn)，但是相比于上述的时间复杂度可以忽略不计
# O(2^n*n)

# 空间复杂度：
# 1. 递归调用栈的深度最大为n
# 2. 假设组合数为m，每个组合的平均长度为k，那么组合的空间复杂度为O(mxk)
# 最坏情况下m=2^n，k接近n，那么空间复杂度为O(2^n*n)


class Solution(object):
    def backtracking(self, result, path, target, candidates, startIndex):
        if sum(path)>target:
            return 
        if sum(path)==target:
            result.append(path[:])
            return
        
        for i in range(startIndex, len(candidates)):
            # 剪枝操作，跳过重复的数字
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            # 注意这里是i+1，因为每个数字都只能使用一次
            self.backtracking(result, path, target, candidates, i+1)
            path.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates=sorted(candidates)
        # sort(candidates)
        self.backtracking(result, [], target, candidates, 0)
        return result
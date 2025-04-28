# 时间复杂度：O(2**n*n)
# 1. 回溯树的节点数量：最坏情况下，回溯算法会生成一个高度为n的决策树，每个元素都存在被选取或者不被选取两种可能，所以这颗决策树的节点总数近似为2**n
# 2. 复制组合：result.append(path[:])有一个复制操作，这个时间复杂度为O(n)
# 空间复杂度：O(n)
# 1. 递归栈大的深度：回溯算法借助递归实现，递归栈的最大深度为n
# 2. 存储路径的空间：path用于存储当前的组合，最坏情况下组合长度达到n
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        candidates.sort()
        self.traversal(result, path, candidates, target, 0)
        return result
    
    def traversal(self, result, path, candidates, target, startIndex):
        if sum(path)==target:
            result.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.traversal(result, path, candidates, target, i+1)
            path.pop()
        
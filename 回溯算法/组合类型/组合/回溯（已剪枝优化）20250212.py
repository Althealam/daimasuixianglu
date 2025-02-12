# 时间复杂度：O(C(n,k)*k) 每个组合需要O(k)的时间来复制到结果集中，并且总共有C(n,k)种组合
# 空间复杂度：O(k)，用于递归调用栈和存储当前组合的path列表


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[] # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        # 1. n表示范围是从1到n的整数
        # 2. k表示需要选取的数字个数
        # 3. startIndex表示当前可以开始选取数字的起始位置
        # 4. path表示当前已经选取的数字组合
        # 5. result表示最终的结果集合，用来存储所有符合条件的组合
        
        # 终止条件：判断是否收获到结果集
        if len(path)==k:
            # 注意这里一定是path[:]，否则path会发生变化的
            result.append(path[:])
            return 
        # 遍历过程
        # 为什么这里是n-(k-len(path))+2
        # 原因：path已经有了len(path)个数字，还需要选择k-len(path)个数字才能满足条件
        # 为了凑齐k个数字，至少还需要k-len(path)个数字
        # 假设当前的数字是i，那么从i到n至少要有k-len(path)个数字
        # 即n-i+1>=k-len(path)-->i<=n-(k-len(path))+1
        # 需要设置终止值为n-(k-len(path))+2，由此可以确保i取到n-(k-len(path))+1
        for i in range(startIndex, n-(k-len(path))+2): # 剪枝的地方
            path.append(i) # 处理节点，将当前的节点i加到path中
            # 调用backtracking方法，继续从i+1开始选取数字，避免重复选取
            self.backtracking(n, k, i+1, path, result)
            path.pop() # 回溯，将当前数字从path中移除
        
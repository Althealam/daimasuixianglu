# 思路：
# 1. 递归函数的参数和返回值：
# path路径，result结果集，k组合大小，n相加之和，startIndex下一层搜索的位置
# 2. 递归的终止条件：
# if sum(path)==n and len(path)==k: result.append(path[:]) return
# 3. 单层搜索的逻辑：将i遍历startIndex到9，path中增加i，递归，弹出元素进行回溯

# 时间复杂度：O(C(9,k)*k)
# 要遍历C(9,k)种组合，并且对每个组合进行O(k)的操作

# 空间复杂度：O(k)
# 1. 递归调用栈的深度为k
# 2. 存储路径path的空间为k

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backtracking(k,n,[],result,1)
        return result
    
    def backtracking(self, k, n, path, result, startIndex):
        if len(path)==k and sum(path)==n:
            result.append(path[:])
            return 
        
        for i in range(startIndex, 10):
            path.append(i)
            self.backtracking(k,n,path,result,i+1)
            path.pop()
        
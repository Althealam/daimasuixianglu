# 方法：回溯方法（未剪枝优化）
# 注意：不能使用暴力方法，因为暴力方法无法控制嵌套的数量（结果长度为k，那么嵌套的for循环就为k）
# 分析：
# 可以将回溯问题看作是一个n叉树，达到叶子结点时收割结果，收割完结果后回溯到父节点，继续开始遍历到叶子结点
# 1. 递归函数的参数和返回值：将一个组合理解为一个一维数组，一维数组记录为path；利用二维数组记录返回值，也就是[[1,2],[1,3],..]这种东西；n是n叉树的根节点的数目；startindex需要用来记录搜索的起始位置
# 2. 确定终止条件：if len(path)==k 即到达叶子结点时开始收集结果
# 3. 确定单层递归的逻辑：从startIndex开始，逐个收集结点

# 时间复杂度：O(C(n,k)*k)，其中C(n,k)是从n中选出k个元素的组合数
# 1. 组合数的计算：O(C(n,k)),n表示可以选择的数字范围，k是每次组合中选取的元素个数
# 每次递归函数都会向path中添加一个元素，然后递归调用下一级，直到长度达到k
# 2. 每次递归的操作：添加和弹出元素，O(1)
# 3. 回溯数的深度：深度为k，相当于路径的长度，也就是你需要组合的数组的大小

# 空间复杂度：O(k+C(n,k)*k)，k是递归栈的深度和每个组合的大小
# 1. 递归栈的深度：递归深度为k，即递归函数调用的最大深度是k
# 2. 存储结果的空间：
# （1）存储所有组合的结果，需要一个二维数组来存储所有的组合，每一个组合是一个长度为k的数组
# （2）存储结果的空间：存储所有组合的结果，需要一个二维数组来存储所有的组合，每个组合是一个长度为k的数组
#     总的组合数是C(n,k)，每个组合的长度为k，因此存储所有结果的空间复杂度为O(C(n,k)*k)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[] # 存放结果集，是一个二维数组
        self.backtracking(n,k,1,[],result)
        # path是一个一维数组[]
        # 由于返回的是[1,n]内的所有可能的k个数的组合，因此起始的startIndex一定是1
        return result

    def backtracking(self,n,k,startIndex,path,result):
        if len(path)==k: # 到达叶子结点，收割结果
            result.append(path[:])
            return
        for i in range(startIndex,n+1): # range(a,b+1)的范围是[a,b]
            path.append(i) # 加入结点到path中 
            self.backtracking(n,k,i+1,path,result)
            path.pop() # 回溯，撤销处理的结点

        
# 方法：回溯法（未进行剪枝）
# 任何回溯算法的题目都可以抽象为一个树形结构
# 分析：路径的深度是由k决定的，每一条路径都是取一个节点；树的宽度则是由取数范围决定的，这里是[1,9]，那么树的宽度是9

# 时间复杂度：O(9,k)
# 1. 回溯树的构建：将所有的可能组合视为一颗树，每一层代表选择数字的一个决策。
# 树的总深度为k，树的宽度为每层的选择树逐层递减，因此回溯树的节点数量最多为C(9,k)
# 2. 回溯过程中每次操作的代价：
# （1）将当前数字加入路径
# （2）判断当前路径是否符合条件（长度是否为k，和是否为targetSum）
# （3）回溯时移除当前数字并计算更新路径和

# 空间复杂度：O(k+C(9,k)*k)
# 1. 递归栈：深度为k
# 2. 存储路径：路径最多有k个元素，O(k)
# 3, 存储结果：每个组合最多有k个数组，最多有C(9,k)个组合，因此存储结果的空间复杂度为O(C(9,k)*k)
class Solution(object):
    def backstracking(self,targetSum,k,sum,startIndex,path,result):
        """
        startIndex控制组合开始的数字
        sum是目前的path里面的总和
        path是我们一条路径上的节点数组
        targetSum是我们的目标和
        """
        if len(path)==k:
            if sum==targetSum:
                result.append(path[:])
        for i in range(startIndex,10):
            sum+=i # 计算路径和
            path.append(i) # 收集路径的节点
            self.backstracking(targetSum,k,sum,i+1,path,result) # 下一条路径
            # 回溯过程（需要从孩子结点回溯到父结点）
            sum-=i 
            path.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backstracking(n,k,0,1,[],result)
        return result

        
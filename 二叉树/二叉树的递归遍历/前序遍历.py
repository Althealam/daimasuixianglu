# 递归的三要素：
# 1. 确定递归函数的参数和返回值：确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数，并且还要明确每次递归的返回值是什么，进而确定递归函数的类型
# 2. 确定终止条件：写完递归函数运行的时候，如果遇到栈溢出的错误，就是没写终止条件或者终止条件不对
# 3. 确定单层递归的逻辑：确定每一层递归需要处理的信息

class Solution:
    def preorderTraversal(self,root: TreeNode)->List[int]:
        res=[]
        
        def dfs(node):
            if node is None:
                return
        
            res.append(node.val) # 中间节点
            dfs(node.left) # 左节点
            dfs(node.right) # 右节点
        dfs(root) # root就是一个根节点
        return res
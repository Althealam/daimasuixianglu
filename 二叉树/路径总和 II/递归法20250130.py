# 思路：本题和二叉树的所有路径类似，但是不同的是这里需要记录下来路径和为targetSum的路径

# 时间复杂度：O(n^2) 对每个节点都需要进行一次O(n)的路径和计算和路径复制操作
# 1. 遍历节点：O(n)
# 2. 计算路径和：O(n)
# 3. 复制路径：O(n)
# 空间复杂度：最坏情况是O(n)，平均情况是O(logn)
# 1. 递归调用栈的空间
# 2. 存储路径的列表空间
# 3. 存储结果的空间列表

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        path=[]
        result=[]
        self.traversal(root, path,result,targetSum)
        return result

    def traversal(self, cur, path, result, targetSum):
        path.append(cur.val)
        
        # 如果到了叶子节点，就要去判断路径和是否为targetSum
        if cur.left is None and cur.right is None:
            if sum(path)==targetSum:
                # 这里必须是添加path[:]，而不是path
                # 易错点：列表是可变对象，使用result.append(path)的时候，是将path列表的引用添加到了result中，而不是path列表的副本，如果后续对path进行了修改，会影响到result
                result.append(path[:])
                return 
        
        # 对左右节点进行遍历
        if cur.left:
            self.traversal(cur.left, path, result, targetSum)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result, targetSum)
            path.pop()
        

        
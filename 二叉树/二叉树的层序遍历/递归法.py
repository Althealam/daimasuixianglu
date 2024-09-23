# 方法二：递归法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 时间复杂度：O(n）（每个节点恰好被访问一次）
# 空间复杂度：O(m）（树的最大层中节点的个数）
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: # 如果根节点为空，就返回一个空列表
            return []
        levels=[] # 初始化一个空列表levels，用于存储层序遍历的结果
        def traverse(node,level): # 递归辅助函数
            if not node: 
                return 
            # 如果levels列表的长度等于当前层级level，则向levels中添加一个新的空列表，用于存储当前层级的节点值
            if len(levels)==level:
                levels.append([])
                
            # 将当前节点的值添加到levels列表的第level个元素中
            levels[level].append(node.val)
            # 递归调用traverse函数，遍历当前节点的左子树，并且层级增加1
            traverse(node.left,level+1)
            # 递归调用traverse函数，遍历当前节点的右子树，并且层级增加1
            traverse(node.right,level+1)

        # 从根节点开始调用traverse函数
        traverse(root,0)
        return levels
# 方法：递归法
# 分析：1. 找到要删除的节点 2. 删除节点（删除节点的步骤最麻烦）
# 第一种情况：没有找到要删除的节点--直接返回即可
# 第二种情况：要删除的节点是叶子结点--直接删除即可
# 第三种情况：要删除的节点的左右孩子节点不为空--大幅度修改二叉树的结构，要把左子树放在右子树的最左边节点
# 第四种情况：要删除的节点左孩子节点不为空，右孩子节点为空--直接让要删除的节点的父节点指向左孩子节点
# 第五种情况：要删除的节点左孩子节点为空，右孩子节点为空--直接让要删除的节点的父节点指向右孩子节点

# 时间复杂度：
# 查找要删除的节点：需要遍历到目标节点的位置
# 调整节点：找到要删除节点后，如果该节点的左右子树都不为空，需要在右子树中找到最左节点，将其连接到左子树上
# 1. 平均情况：树是平衡的，O(logn)
# 2. 最坏情况：树是完全不平衡的，O(n)

# 空间复杂度：取决于递归调用的深度
# 1. 平均情况：O(logn)
# 2. 最坏情况：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root==None:
            return None
        if root.val==key:
            if root.left==None and root.right==None: # 要删除的节点为叶子结点
                return None # 后面会有一层用来接收该返回值
            elif root.left!=None and root.right==None: # 要删除的节点左孩子不为空，右孩子为空
                return root.left
            elif root.left==None and root.right!=None: # 要删除的节点左孩子为空，右孩子不为空
                return root.right
            else: # 要删除的节点左右孩子都不为空（把左子树放在右子树的最左节点）
                # 对右子树进行处理
                cur=root.right # 利用cur记录右子树的最左节点
                while cur.left!=None:
                    cur=cur.left
                cur.left=root.left 
                return root.right

        # 单层递归的逻辑
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        return root




        
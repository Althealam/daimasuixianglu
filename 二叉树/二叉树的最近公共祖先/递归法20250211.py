# 思路：如何判断某个节点是节点p和节点q的公共祖先
# 1. 某个节点的左子树出现节点p，右子树出现节点q
# 2. 某个节点的左子树出现节点q，右子树出现节点p

# 递归法：
# 1. 确定递归函数返回值以及参数：需要递归函数的返回值来告诉我们是否找到了节点p和节点q
# 2. 终止条件：树为空的时候返回空
# 如果root==q, root==q，表示找到了p和q，则将其返回
# 3. 单层递归的逻辑：递归函数有返回值就是要遍历某一条边

# 采用后序遍历的思想，因为后序遍历是从下往上遍历的，可以帮助我们找到最近的公共祖先

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==q or root==p or root is None:
            return root
        # 1. root is None：遍历到树的叶子节点之外，还没找到节点p或者q，直接返回None
        # 2. root==p：代表找到了一个目标节点
        # 3. root==q：代表找到了一个目标节点
        # 如果另外一个目标节点在该节点的子树中，那么这个节点就是它们的最近公共祖先
        # 如果另外一个目标节点不在该节点的子树中，后续递归会在其他分支找到它，然后通过回溯来确定最终的公共祖先

        left=self.lowestCommonAncestor(root.left, p, q) # 存储左子树找到的目标节点或者最近公共祖先
        right=self.lowestCommonAncestor(root.right, p, q) # 存储右子树找到的目标节点或者最近公共最先

        # 中间节点的逻辑处理，回溯
        # 1. left和None都不为None，表示在左子树中找到了一个目标节点，在右子树中找到了一个目标节点，当前root就是目标节点的最近公共祖先（从当前节点开始，两个目标节点分别位于左右子树中）
        if left is not None and right is not None:
            return root
        
        # 2. left为None表示在左子树中没有找到目标节点；right不为None表示在右子树中找到了目标节点。
        # 那么最近的公共祖先就在右子树中，返回right
        if left is None and right is not None:
            return right
        # 3. left不为None表示在左子树中找到了目标节点；right为None表示在右子树中没有找到目标节点。
        # 那么最近的公共祖先就在左子树中，返回left
        elif left is not None and right is None:
            return left
        # 4. left和right都为None表示当前节点的左右子树中都没有找到目标节点
        else:
            return None
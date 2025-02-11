# 思路：
# 1. 没有找到需要修剪的节点，返回None
# 2. root.val<low：root的左子树也一定小于low，可以直接剪去，检查右子树即可
# 3. root.val>low：root的右子树也一定大于low，可以直接剪去，检查左子树即可

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：修剪过程中需要遍历二叉搜索树中的每个节点，判断该节点的值是否在区间内，因此是O(n)
# 空间复杂度：O(1)，没有递归调用栈，只是使用了cur

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # 处理头节点，让root移动到[L,R]区间内
        while root and (root.val<low or root.val>high):
            # 如果root的值小于low，那么root的左子树一定都小于low，那么往右边走
            if root.val<low:
                root=root.right
            # 如果root的值大于high，那么root的右子树一定都大于high，那么往左边走
            elif root.val>high:
                root=root.left
        
        # 继续处理后面的节点，此时的root已经在[low, high]区间内
        
        # 1. 处理左子树
        cur=root
        while cur:
            # 左孩子存在并且左孩子的节点值小于low，那么左孩子的左孩子也是不符合的，那么将左孩子变成左孩子的右子树即可
            while cur.left and cur.left.val<low:
                cur.left=cur.left.right
            # 继续处理左子树
            cur=cur.left
        
        # 2. 处理右子树
        cur=root
        while cur:
            # 右孩子存在并且右孩子的节点值大于high，那么右孩子的右孩子也是不符合的，那么将右孩子变成右孩子的左孩子即可
            while cur.right and cur.right.val>high:
                cur.right=cur.right.left
            # 继续处理右子树
            cur=cur.right
        
        return root


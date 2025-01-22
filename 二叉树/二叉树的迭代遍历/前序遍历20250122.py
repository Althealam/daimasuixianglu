# 前序遍历：先将根节点放入结果列表中，然后将右节点入栈，再加入左节点
# 注意：
# 1. 放到result结果列表里的是节点的值(node.val），而放到stack栈里的是节点（node）
# 2. 一定是右孩子先入栈，然后再是左孩子入栈，因为前序遍历是中左右，右孩子先入栈的话就会最后一个出来

# 时间复杂度：O(n)
# 空间复杂度：O(logn) 取决于栈stack的大小，最好的情况下二叉树是完全平衡的

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def preorderTraversal(self, root):
        # 根节点为空的时候直接返回空列表
        if not root:
            return []
        stack=[root] # 用来将节点放入栈
        result=[] # 用来记录最后输出的前序遍历
        while stack:
            node=stack.pop()
            # 中节点放到result里
            result.append(node.val)
            # 右孩子入栈
            if node.right:
                stack.append(node.right)
            # 左孩子入栈
            if node.left:
                stack.append(node.left)
            print(result)
        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s=Solution()
print(s.preorderTraversal(root))


# 后序遍历是左右中，可以通过先序遍历是中、右、左（左孩子先入栈，右孩子后入栈），然后把数组反过来即可
# 为什么把数组反过来可以实现？
# 可以联想一下，一开始是123，反过来后会变成321，也就是中右左会变成左右中（分别对应123）

# 时间复杂度：O(n)
# result[::-1]会对数组进行反转的操作，这时候的时间复杂度是O(n)
# 空间复杂度：O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            node=stack.pop()
            result.append(node.val)
            while node.left:
                stack.append(node.left)
            while node.right:
                stack.append(node.right)
        return result[::-1] # 翻转数组
    
   
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s=Solution()
print(s.postorderTraversal(root))



# 后序遍历
# 先递归进行左子树的后序遍历，然后递归的进行右子数的后序遍历，最后访问根节点
class Solution:
    def postorderTraversal(self, root: TreeNode)->List[int]:
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            # 先处理中节点
            node=stack.pop()
            result.append(node.val)
            # 先是左孩子入栈，再是右孩子入栈，这样result的顺序会是中右左，将result进行翻转就可以得到左右中
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]
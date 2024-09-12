# 前序遍历（和后序遍历是类似的,只不过最后输出的数组会经过翻转）
# 非递归法就是迭代法
# 思路：利用一个栈来模拟递归的过程
class Solution:
    def preorderTraversal(self, root:TreeNode)->List[int]:
        # 根节点为空则返回空列表
        if not root:
            return []
        stack=[root] # 将根节点入栈
        result=[] # 用于存放遍历的结果
        while stack: # 循环处理栈
            # 中节点先处理
            node=stack.pop() 
            result.append(node.val)
            # 先进右节点再进左节点，这是因为栈是先进后出的顺序
            # 右孩子入栈
            if node.right:
                stack.append(node.right)
            # 左孩子入栈
            if node.left:
                stack.append(node.left)
        return result
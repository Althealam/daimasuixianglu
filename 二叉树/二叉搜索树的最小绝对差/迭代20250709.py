# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：通过中序遍历获取二叉搜索树的数组，然后计算两两节点之间的差，选择最小的作为两值之差的最小值
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = self.inorder(root)
        ans = float('inf')
        for i in range(1, len(res)):
            ans = min (ans, res[i]-res[i-1])
        return ans
    
    def inorder(self, root):
        if not root:
            return []
        st = [root]
        res = []
        while st:
            node = st.pop()
            if node:
                if node.right:
                    st.append(node.right)
                st.append(node)
                st.append(None)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                res.append(node.val)
        return res
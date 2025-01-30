# 思路：层序遍历，找到最后一行，然后找到最后一行最左边的值
# 层序遍历怎么判断是否达到最后一行：可以不用判断是否达到最后一行，遍历每一行的时候存储最左边的值即可
# 层序遍历最后一行怎么判断是否是最左边的值：判断i是否为len(queue)-1
# 时间复杂度：O(n)
# 空间复杂度：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue=collections.deque([root])
        leftarray=[]
        while queue:    
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==0:
                    leftarray.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftarray[-1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 时间复杂度：O(n)，n是二叉树中节点的总数（因为每个节点恰好被访问一次）
# 空间复杂度：O(m)，m是树的最大宽度（树的最大层中节点的数量）
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # 初始化一个双端队列queue，并将根节点加入队列
        # collections.queue是python标准库中的一个双端队列实现
        queue=collections.deque([root])
        # 初始化一个空列表，用于存储层序遍历的结果
        result=[]
        while queue:
            level=[] # 每次循环的开始，初始化空列表，用于存储当前层的节点
            for _ in range(len(queue)): # 使用一个循环，遍历当前队列中的所有节点
                cur=queue.popleft() # 从队列的左侧弹出一个节点
                level.append(cur.val) # 将当前节点的值赋给level列表
                if cur.left: # 如果当前节点有左子节点，就添加到队列中
                    queue.append(cur.left)
                if cur.right: # 如果当前节点有右子节点，就添加到队列中
                    queue.append(cur.right)
            result.append(level) # 将当前层的节点值列表lebel添加到结果列表result中
        return result[::-1] # 将结果列表level反转，使得第一层在最后
        
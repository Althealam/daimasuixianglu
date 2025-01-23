# 思路：使用层序遍历，并且记录层数即可
# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth=0
        if not root:
            return depth
        queue=collections.deque([root])
        while queue:
            depth+=1
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        return depth

def list_to_tree(lst): 
    if not lst:
        return None
    root=TreeNode(lst[0]) # 根节点
    queue=collections.deque([root]) # 用队列来存储列表中的元素，也就是层序遍历的值
    i=1
    while queue and i<len(lst):
        node=queue.popleft()
        if lst[i] is not None:
            node.left=TreeNode(lst[i])
            queue.append(node.left)
        i+=1 # 记录已经遍历的节点数（这个节点数就是遍历到列表的节点数），不管lst[i]是否空节点，都需要去记录已经遍历的节点数
        if i<len(lst) and lst[i] is not None:
            node.right=TreeNode(lst[i])
            queue.append(node.right)
        i+=1
    return root



root=[1,2,3,4,5]
tree=list_to_tree(root)
solution=Solution()
depth=solution.maxDepth(tree)
print(depth)

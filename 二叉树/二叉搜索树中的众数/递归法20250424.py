# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vector=[]
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.traversal(root, self.vector)
        cnt=defaultdict(int)
        result=[] # 统计出现频率最高的节点的值
        for v in self.vector:
            if v not in cnt:
                cnt[v]=1
            else:
                cnt[v]+=1
        
        max_freq=max(cnt.values())

        for v in cnt.keys():
            if cnt[v]==max_freq:
                result.append(v)
        return result
    
    def traversal(self, node, vector):
        if node.left:
            self.traversal(node.left, vector)
        vector.append(node.val)
        if node.right:
            self.traversal(node.right, vector)

    

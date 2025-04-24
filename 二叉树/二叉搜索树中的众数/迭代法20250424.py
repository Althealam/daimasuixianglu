# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack=[]
        prev=None # 上一个节点
        cur=root # 当前遍历的节点
        result=[] # 众数
        max_count=0 # 统计最大的出现频率
        count=0 # 统计该元素值出现的频率
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                # 判断上一个节点的值和这个节点的值的情况
                # 1. 上一个节点不为空并且和当前节点的值相同
                if prev and prev.val==cur.val:
                    count+=1
                # 2. 上一个节点不为空并且和当前节点的值不同
                elif prev and prev.val!=cur.val:
                    count=1
                # 3. 上一个节点为空，也就是当前节点是第一个节点
                else:
                    count=1
                if count==max_count:
                    result.append(cur.val)
                if count>max_count:
                    max_count=count
                    result=[cur.val] # 清空result数组
                # 移动prev和cur
                prev=cur
                cur=cur.right
        return result
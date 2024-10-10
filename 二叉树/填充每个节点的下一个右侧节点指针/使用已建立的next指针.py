# 方法：使用已建立的next指针
# 分析：一棵树中存在两种类型的next指针
# 1. 连接同一个父节点的两个子节点，它们可以通过同一个节点直接访问到，因此执行node.left.next=node.right即可
# 2. 不同父亲的子节点之间建立连接：
# 第N层节点之间建立next指针之后，再建立N+1层节点的next指针。可以通过next指针访问同一层的所有节点，因此可以使用第N层的next指针，为第N+1层节点建立next指针
# 时间复杂度：O(n)，每个节点只访问一次
# 空间复杂度：O(1)，不需要存储额外的节点
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        # 从根节点开始
        leftmost=root

        while leftmost.left:
            # 遍历这一层节点组织乘的链表，为下一层的节点更新next指针
            head=leftmost
            while head:
                # connection 1
                head.left.next=head.right
                # connection 2
                if head.next:
                    head.right.next=head.next.left
                
                # 指针向后移动
                head=head.next
            
            # 去下一层的最左的节点
            leftmost=leftmost.left
        return root
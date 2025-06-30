# 方法：遍历法（龟兔赛跑算法）
# 思路：在循环过程中把所有节点的指针都存在集合中，如果发现某个节点的next指针已经在集合中了，那就意味着这个next之前遍历过，现在又遍历回来了，那这个next就是环形的入环处
# 时间复杂度：O(n) 
# 空间复杂度：O(n)，集合S需要存储所有n个节点

# Definition for singly-linked list.
# # class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        S=set()
        move=head
        while move:
            if move.next in S:
                return move.next
            S.add(move)
            move=move.next
        return None
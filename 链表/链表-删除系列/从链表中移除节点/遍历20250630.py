# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [5, 2, 13, 3, 8]
# [5, 13, 8]
# [13, 8]

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        node=self.removeNodes(head.next) # 返回的链表头一定是最大的
        if node.val>head.val:
            return node # 删除head
        head.next=node # 不删除head
        return head
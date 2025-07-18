# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        fast, slow = dummy_node, dummy_node
        for _ in range(n):
            fast = fast.next
        
        # 找到需要被删除的节点的前面一个节点
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
    
        slow.next = slow.next.next

        return dummy_node.next

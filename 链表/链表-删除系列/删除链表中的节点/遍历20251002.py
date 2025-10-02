# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        cur = dummy_node
        while cur and cur.next:
            if cur.next.val==val:
                nxt = cur.next.next
                cur.next = nxt
            cur = cur.next
        return dummy_node.next
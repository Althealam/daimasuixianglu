# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        cur = dummy_node
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.val==cur.next.next.val:
                while cur.next and cur.next.val==val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_node.next
        
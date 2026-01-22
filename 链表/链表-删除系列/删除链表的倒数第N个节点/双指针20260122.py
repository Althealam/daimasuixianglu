# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        # we must start with the dummy_node, because the first node may be the node need to delete
        slow, fast = dummy_node, dummy_node
        for _ in range(n):
            fast = fast.next

        # find the delete node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # remove the node
        slow.next = slow.next.next

        return dummy_node.next
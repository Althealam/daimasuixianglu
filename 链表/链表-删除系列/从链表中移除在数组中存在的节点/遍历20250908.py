# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        st = set(nums)
        cur = dummy_node

        while cur.next:
            if cur.next.val in st:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_node.next
        
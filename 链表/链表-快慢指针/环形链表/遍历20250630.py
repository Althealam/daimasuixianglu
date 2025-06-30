# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：定义快慢指针，快指针每次走两步，慢指针每次走一步，如果有环，那么快慢指针会相遇
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
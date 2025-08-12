# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个新链表
        dummy_node = ListNode()
        cur = dummy_node
        carry = 0 # 进位值
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry//=10
            cur = cur.next
        return dummy_node.next
            
        
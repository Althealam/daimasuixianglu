
class Solution:
    # l1和l2为当前遍历的节点，carry为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0 # 进位值
        while l1 or l2 or carry: # 有一个不是空节点，或者还有进位，则继续迭代
            if l1:
                carry+=l1.val # 节点值和进位值加载一起
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry //=10 # 新的进位
            cur = cur.next
        return dummy.next
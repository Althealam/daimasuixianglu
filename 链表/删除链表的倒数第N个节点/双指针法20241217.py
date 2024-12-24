# 思路：
# 定义快慢指针fast和slow，并制造相对位置差，也就是在一开始的时候fast指针就比slow指针多走n步
# 当fast走到null的时候，slow刚好指向需要删除的节点的前一个节点，这时候删除即可

# 时间复杂度：O(n)
# 空间复杂度：O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy_head=ListNode(0,head)
        i=0
        # 定义快慢指针
        slow=dummy_head
        fast=dummy_head
        # 移动fast指针，构造位置差
        while i<=n:
            fast=fast.next
            i+=1
        # 构造完位置差以后，开始遍历slow和fast
        while fast:
            slow=slow.next
            fast=fast.next

        # 删除slow的下一个节点（当fast刚好达到null的时候，slow指向的是需要被删除的节点的前一个节点）
        slow.next=slow.next.next

        return dummy_head.next

        
# 方法二：递归版本
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # 待翻转的两个node分别是pre和cur
        pre=head
        cur=head.next
        next=head.next.next

        cur.next=pre
        pre.next=self.swapPairs(next) # 以next为head的后续链表两两交换
        
        return cur


        
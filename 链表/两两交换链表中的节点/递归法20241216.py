# 思路：递归法
# 1. 链表中没有节点：结束
# 2. 链表中只有一个节点：返回原来的head
# 3. 链表中有两个节点：原来的head变成新链表的第二个节点，原来的第二个节点变成newhead
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(n)，空间复杂度取决于递归调用的栈空间

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 链表只有一个节点，或者链表为空
        if not head or not head.next:
            return head

        # 只有两个节点时，newhead是第二个节点，并且newhead会成为新的头节点
        newhead=head.next
        head.next=self.swapPairs(newhead.next)
        # 只有两个节点时，交换newhead和head
        newhead.next=head
        return newhead # 新的头节点
        
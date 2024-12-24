# 思路：定义一个pre和cur，正常来说是pre.next=cur，但是我们可以改成cur.next=pre
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)

# 注意：不能去定义一个虚拟头节点，然后让虚拟头节点指向head，否则会导致在反转链表的操作时出现问题

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        pre=None
        while cur:
            # 保存cur的下一个指针
            temp=cur.next
            # 开始反转链表
            cur.next=pre
            # 修改cur和pre
            pre=cur
            cur=temp
        return pre

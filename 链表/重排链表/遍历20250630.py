# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 找到链表的中间节点
# 2. 将链表的后半段反转
# 3. 将反转后的链表后半段和链表前半段合并在一起
# （1）反转的链表的头节点为head2，前半段链表的头节点为head1

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def middleNode(self, head):
        # 1. 找链表的中间节点
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # slow到达的位置就是链表的中间节点
        return slow

    def reverseList(self, head):
        # 2. 反转slow后面的链表
        pre=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid=self.middleNode(head)
        head2=self.reverseList(mid)
        while head2.next:
            # 提前记录两半段链表的下一个节点
            nxt=head.next
            nxt2=head2.next
            # 移动两个指针，将两段链表插入在一起
            head.next=head2
            head2.next=nxt
            # 移动head和head2，开始下一次遍历
            head=nxt
            head2=nxt2
    

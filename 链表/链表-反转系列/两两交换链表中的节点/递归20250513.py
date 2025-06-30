# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：保存两个待翻转的节点
# step1：让第一个待翻转的节点前面的节点指向第二个待翻转的节点后面的节点
# step2：让第二个待翻转的节点指向第一个待翻转的节点
# step3：让第一个待翻转的节点连接到第二个待翻转的节点后面的节点
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 待翻转的节点分别是pre和cur
        pre=head
        cur=head.next
        nxt=head.next.next

        # 开始反转节点
        cur.next=pre
        pre.next=self.swapPairs(nxt) # 将以nxt为head的后续链表进行两两交换
        return cur
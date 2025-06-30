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
        dummy_node=ListNode(next=head)
        cur=dummy_node
        while cur.next and cur.next.next:
            temp=cur.next 
            temp1=cur.next.next.next
            # step1：更改cur指向的节点
            cur.next=cur.next.next
            # step2：更改两个节点之间的顺序
            cur.next.next=temp
            # step3：连接起来反转的地方
            temp.next=temp1
            # step4：移动cur
            cur=cur.next.next
        return dummy_node.next

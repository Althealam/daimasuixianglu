# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        pre=None
        while cur:
            tmp=cur.next # 保存cur的下一个节点
            cur.next=pre # 反转节点
            # 更新pre和cur的指针
            pre=cur
            cur=tmp
        return pre


            
        
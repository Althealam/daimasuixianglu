# 方法二：不设置虚拟头节点
# 时间复杂度：O(n) 遍历整个链表来检查每个节点的数量
# 空间复杂度：O(1) 存储指针变量个
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val # 数据域 
#         self.next = next # 指针域
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 处理头节点就是要删除的节点的情况
        while head is not None and head.val==val:
            head=head.next
        
        # current用于遍历链表
        current=head
        while current is not None and current.next is not None:
            if current.next.val==val:
                current.next=current.next.next # 删除当前节点的下一个节点
            else:
                current=current.next
            
        return head
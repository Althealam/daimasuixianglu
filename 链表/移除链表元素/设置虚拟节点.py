# 方法一：设置虚拟节点
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
        # 创建虚拟头部节点以简化删除过程
        dummy_head=ListNode(next=head)

        # 遍历列表并删除值为val的节点
        current=dummy_head
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next

        return dummy_head.next
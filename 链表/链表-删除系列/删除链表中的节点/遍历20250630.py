# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：1. 直接copy下一个节点的节点值到该节点 2. 将该节点的next指针指向下下个节点，也就是删除掉node的下一个节点
# 时间复杂度：O(1)
# 空间复杂度：O(1)

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
        
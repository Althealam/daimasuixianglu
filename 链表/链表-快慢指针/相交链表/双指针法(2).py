# 思路：求两个链表交点的指针（交点指的是两个链表共享的节点，而不只是数值相同）
# 通过调整两个指针的起始位置，使得它们在同一起点开始遍历，这样它们会在交点相遇
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 时间复杂度：O(L+M)，L和M分别是两个链表的长度
# 空间复杂度：O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA=0 # 初始化链表A的长度为0
        lenB=0 # 初始化链表B的长度为0
        cur=headA
        while cur: # 求链表A的长度
            cur=cur.next
            lenA+=1
        cur=headB
        while cur: # 求链表B的长度
            cur=cur.next
            lenB+=1
        curA, curB = headA, headB

        # 找最长链表，并且让curB指向最长链表的头，让lenB表示最长链表的长度
        while lenA>lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA

        for _ in range(lenB-lenA): # 让curA和curB在同一起点上（剩下需要遍历的节点个数是相同的，都是lenA）
            curB=curB.next
        while curA: # 遍历curA和curB，遇到相同的则直接返回
            if curA==curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None
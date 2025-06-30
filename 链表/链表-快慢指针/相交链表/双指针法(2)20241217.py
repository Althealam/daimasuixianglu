# 思路：
# 1. 先求出链表A和B的长度
# 2. 假设链表长度比较长的是B，让B的指针pB先移动到和pA一样的开始位置
# 3. 同步移动pA和pB，如果遇到pA==pB，则返回，一直没有的话就返回NULL

# 时间复杂度：O(m+n)
# 空间复杂度：O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA, lengthB=0,0
        # 求链表A和链表B的长度
        cur=headA
        while cur:
            cur=cur.next
            lengthA+=1
        cur=headB
        while cur:
            cur=cur.next
            lengthB+=1
        curA, curB= headA, headB
        # 让curB为最长链表的头节点，lengthB为最长链表的长度
        if lengthA>lengthB:
            curA, curB=curB, curA
            lengthA, lengthB=lengthB, lengthA
        # 移动最长链表的指针
        for _ in range(lengthB-lengthA):
            curB=curB.next
        while curA:
            if curA==curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None
        
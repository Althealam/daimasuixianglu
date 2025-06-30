# 思路：
# A链表不相交部分为l1，B链表不相交部分为l2，共同部分为common
# l1+common+l2=l2+common+l1
# 如果不相交，那么common=0


# 时间复杂度：O(m+n)，其中m是链表A的长度，n是链表B的长度
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
        if headA==None or headB==None:
            return None
        pA=headA        
        pB=headB
        # 遍历两个链表直到节点相交
        while pA!=pB:
            pA=pA.next if pA else headB
            pB=pB.next if pB else headA
        return pA


        
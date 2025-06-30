# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：
# 1. 求出A和B的链表长度
# 2. 移动比较长的链表的head节点，直到两个链表指针后面的长度相同
# 3. 同步移动指针，直到指向的节点相同

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 求出A和B的链表长度
        lengthA=self.getheight(headA)
        lengthB=self.getheight(headB)

        # 移动链表的头指针
        if lengthA>lengthB:
            headA=self.moveforward(headA, lengthA-lengthB)
        else:
            headB=self.moveforward(headB, lengthB-lengthA)
        
        # 查找相交节点
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        
        # 没有相交节点
        return None
        
    
    def getheight(self, head):
        length=0
        while head:
            length+=1
            head=head.next
        return length
        
    def moveforward(self, head, steps):
        while steps>0:
            head=head.next
            steps-=1
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)
        if lengthB>lengthA:
            headA, headB = headB, headA
        
        diff_length = abs(lengthA-lengthB)

        curA= headA
        curB = headB
        for _ in range(diff_length):
            curA = curA.next
        
        while curA and curB:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
        
        return None
    
    def get_length(self, head):
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length+=1
        return length
        
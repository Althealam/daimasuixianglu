# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)
        # make the list A be the longest link
        if lengthA<lengthB:
            headA, headB = headB, headA
            lengthA, lengthB = lengthB, lengthA
        diff = lengthA-lengthB

        # get to the node with the same length
        curA, curB = headA, headB
        for _ in range(diff):
            curA = curA.next

        while curA!=curB: # not the value, is node
            curA = curA.next
            curB = curB.next
        
        return curA

    
    def get_length(self, head):
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        return length
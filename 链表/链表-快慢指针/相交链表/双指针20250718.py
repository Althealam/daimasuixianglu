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
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)
        # 让A为最长的链表
        if lengthB>lengthA:
            headA, headB = headB, headA
        
        # 开始求出距离差
        diff_length = abs(lengthA-lengthB)

        # 让A的节点先走一部分
        curA = headA
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
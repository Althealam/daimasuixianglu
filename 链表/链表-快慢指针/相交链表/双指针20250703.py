# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：
# 1. 求出两个链表的长度
# 2. 定义双指针，让长链表的指针先走
# 3. 让两个指针共同出发，如果遇到了相同的节点，则是相交的

# 时间复杂度：O(m+n) 其中m是headA的长度，n是headB的长度
# 空间复杂度：O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length1 = self.get_length(headA)
        length2 = self.get_length(headB)
        # 让headB为长度更长的链表，headA为相对更短的链表
        if length2<length1:
            headB, headA = headA, headB
            length2, length1 = length1, length2
        length = abs(length2-length1)
        cur1 = headA
        cur2 = headB
        for _ in range(length):
            cur2 = cur2.next
        
        while cur1 or cur2:
            if cur1==cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        return None

    
    def get_length(self, head):
        cur = head
        length = 0
        while cur:
            cur = cur.next 
            length+=1
        return length
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. 定义slow和fast，让fast每次走两步，slow每次走一步，最后slow和fast相遇的话则找到了相遇点
# 2. 让head从头节点触发，当slow从相遇点出发，最后slow和head会在环的入口相遇
# 假设slow走的节点数为x+y，fast走过的节点数为x+y+n(y+z)，n为fast指针在环内走的圈数
# (x+y)*2 = x+y+n(y+z)==>x+y=n(y+z)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast: # 找到了相遇点
                slow = head
                while fast!=slow: # 还未到达环形链表的入口
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        
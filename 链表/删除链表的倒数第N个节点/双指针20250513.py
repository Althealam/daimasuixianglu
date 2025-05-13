# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：定义双指针fast和slow，然后让fast先走n步，slow和fast同步移动节点，当fast到达最后一个节点时，slow就到达了倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        slow, fast = dummy_node, dummy_node
        # 移动fast节点
        for i in range(n+1):
            fast = fast.next
        # 移动两个节点，当fast到达最后一个节点时，slow指向倒数第n个节点的前面一个节点
        while fast:
            slow=slow.next
            fast=fast.next
        
        # 删除倒数第n个节点
        slow.next=slow.next.next
        return dummy_node.next

        
        
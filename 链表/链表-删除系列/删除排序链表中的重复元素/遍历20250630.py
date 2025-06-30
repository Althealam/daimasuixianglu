# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 分析：由于本题的头节点是可以保存的，因此可以不需要dummy_node
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# 思路：每次都检查是否有下一个节点的存在，然后判断cur和cur.next的值是否相同，如果相同的话则删除cur.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur=head
        while cur.next:
            if cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head
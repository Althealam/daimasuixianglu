# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 定义一个dummy_node, cur（表示需要进行判断的节点的上一个节点）
# 每次遍历的时候都判断一下cur.next和cur.next.next是否相同，如果相同的话则进行删除操作（通过cur来进行删除）直到没有相同元素值的节点

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        cur = dummy_node
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.val==cur.next.next.val:
                while cur.next and cur.next.val==val:
                    cur.next = cur.next.next
            else:
                cur=cur.next
        return dummy_node.next
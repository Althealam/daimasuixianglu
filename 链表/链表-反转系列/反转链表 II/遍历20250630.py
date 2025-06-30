# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 找到需要反转的链表的前一个节点值
# 2. 反转固定位置的链表

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        pre = dummy_head # 移动到需要删除的链表的前面一个节点
        for _ in range(left-1):
            pre = pre.next
        
        # 现在找到了需要反转的链表的前一个节点值 开始反转链表
        cur = pre.next
        for _ in range(right-left):
            # 每次遍历的时候 都需要交换cur和nxt的位置 从pre->cur->nxt->nxt.next变成pre->nxt->cur->nxt.next
            nxt = cur.next # 指向需要反转的链表的第二个节点
            cur.next = nxt.next # pre->cur->nxt->nxt.next ==> 断开cur与nxt之间的连接 pre->cur->nxt.next nxt
            nxt.next = pre.next # nxt.next->cur nxt pre
            pre.next = nxt # pre->nxt->cur->nxt.next 
        
        return dummy_head.next
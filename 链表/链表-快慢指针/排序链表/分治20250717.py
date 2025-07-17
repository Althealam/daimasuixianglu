class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(val = 4)
head.next = ListNode(val=2)
head.next.next = ListNode(val=1)
head.next.next.next = ListNode(3)

class Solution:
    def middle_node(self, head):
        """寻找中间节点"""
        if head is None or head.next is None:
            return head
        fast, slow = head, head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None # 将第一段链表和第二段链表断开
        return slow # slow为第二段链表的开始节点
    
    def sortList(self, head1, head2):
        dummy_node = ListNode()
        cur = dummy_node
        while head1 and head2:
            if head1.val<head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        return dummy_node.next

    def sort_list(self, head):
        if head is None or head.next is None:
            return head
        head2 = self.middle_node(head) # 第二段链表的开始节点
        # 开始排序两个链表
        head2 = self.sort_list(head2)
        head = self.sort_list(head)
        # 合并两个有序链表
        return self.sortList(head, head2)

def print_list(head):
    cur = head
    while cur and cur.next:
        print(str(cur.val)+'->')
        cur = cur.next
    print(cur.val)

sol = Solution()
res = sol.sort_list(head)
print_list(res)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(Llogm)，其中m为lists的长度，L为所有链表的长度之和。每个节点参与链表合并的次数为O(logm)次，一共有L个节点，所以总的时间复杂度为O(Llogm)
# 空间复杂度：O(logm)，递归深度为O(logm)，需要O(logm)的栈空间
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists) # 链表的个数
        if m==0:
            return None
        if m==1:
            return lists[0]
        left = self.mergeKLists(lists[:m//2]) # 合并左半部分
        right = self.mergeKLists(lists[m//2:]) # 合并右半部分
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, list1, list2):
        """合并两个有序链表"""
        cur = dummy = ListNode() 
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1  # 将list1加入到新链表中
                list1 = list1.next
            else:
                cur.next = list2 # 将list2加入到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2 # 拼接剩余链表
        return dummy.next
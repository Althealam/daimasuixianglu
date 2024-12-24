# 方法二：递归法
# 时间复杂度：O(n)
# 空间复杂度：O(n)，递归的深度是n，每层递归都需要存储局部变量和返回地址
# 递归法思想：将问题分解成更小的子问题，然后递归的解决这些子问题，最后将子问题的解合并得到原问题的解
# Definition for singly-linked list.
# class ListNode(object):
# 定义了链表的节点，每一个节点包含一个值val和指向下一节点的指针next
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head): # 对外的接口函数
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 相当于temp=head, cur=None
        return self.reverse(head,None)
    def reverse(self, cur, pre): # 递归方法
        if cur==None:
            return pre
        temp=cur.next
        cur.next=pre
        return self.reverse(temp,cur)


# 思路：双指针法
# 解释：将两个链表连接在一起，就可以得到相交的部分
# 1. 首先是两个链表（约定，值相同代表同一节点，0代表空节点）
# A: [1,2,3,7,8,9]
# B: [4,5,7,8,9]

# 2. 链接两个表（表与表之间用0隔开）
# （1）如果有相交：
# AB: [1,2,3,7,8,9,0,4,5,7,8,9]
# BA: [4,5,7,8,9,0,1,2,3,7,8,9]
# 可以发现，相交的部分整齐的排列在末尾，只要逐个比较这两个表的节点，就能找到相交的起始位置
# （2）如果没有相交：
# A: [1,2,3]
# B: [4,5]
# AB: [1,2,3,0,4,5]
# BA: [4,5,0,1,2,3]
# 可以发现末尾相交的部分为空

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 时间复杂度：O(L+M)，L和M分别是两个链表的长度
# 空间复杂度：O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A,B=headA,headB
        while A!=B: # 节点相等的条件是val和next都相同
            A=A.next if A else headB # 移动A指针遍历AB表
            B=B.next if B else headA # 移动B指针遍历BA表
        return A
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：单调栈，栈中存储没有找到右边更大元素的节点，弹出栈的元素是需要删除的
# 最后判断栈中是否存在节点，如果存在的话那么开始处理栈中节点
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        cur = head
        while cur:
            while st and st[-1].val<cur.val:
                st.pop()
            st.append(cur)
            cur = cur.next
        
        # 栈中还存在元素
        while len(st)>1:
            node = st.pop()
            st[-1].next = node
        return st.pop()
        
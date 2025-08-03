# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：单调栈，栈中存储没有找到右边有更大元素的节点，弹出栈的元素是需要删除的
# 最后判断栈中是否存在元素，如果存在的话，那么开始处理栈中的节点
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        cur = head
        while cur:
            while st and st[-1].val<cur.val: # 当前遇到的元素比栈顶元素大，那么弹出栈顶元素，因为栈顶元素找到了右边的更大元素
                st.pop()
            st.append(cur)
            cur = cur.next
        
        while len(st)>1: # 判断栈中是否还存在元素 并且栈中的最后一个元素就是头元素
            nxt = st.pop()
            st[-1].next = nxt
        return st.pop()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
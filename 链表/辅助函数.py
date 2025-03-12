# 定义链表的节点
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


# 将列表转换为链表
def list_to_linkedlist(lst):
    dummy=ListNode() # 定义一个虚拟头节点
    current=dummy
    for val in lst: # 遍历列表中的元素
        current.next=ListNode(val) # 构建节点
        current=current.next # 移动节点
    return dummy.next # 返回链表

# 打印链表
def print_linkedlist(head_linkedlist):
    current=head_linkedlist
    while current:
        print(str(current.val)+'->')
        current=current.next
    print('None')
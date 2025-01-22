# 中序遍历：先去找到树左边的最底部，然后再开始处理节点（中序遍历是左中右）

# 时间复杂度：O(n)
# 空间复杂度：O(n)，取决于stack的大小，当二叉树退化为链表的时候，栈中最多会存储n个节点
class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def inorderTraversal(self, root):
        # 如果没有根节点，直接返回空列表
        if not root:
            return []
        stack=[]
        result=[]
        cur=root
        stack_num=[]
        while cur or stack:
            if cur:
                # 寻找左子树的最左节点
                stack.append(cur)
                stack_num.append(cur.val)
                cur=cur.left
                print("if cur:")
            else:
                cur=stack.pop()
                result.append(cur.val)
                stack_num.pop()
                # 取栈顶元素的右节点
                cur=cur.right
                print("else")
            print(f"stack_num:{stack_num}")
            print(f"result:{result}")
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s=Solution()
print(s.inorderTraversal(root))







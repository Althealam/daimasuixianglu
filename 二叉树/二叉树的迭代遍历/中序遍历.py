class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 思路：先定义指针指向root，然后让指针一直遍历左节点，直到左节点没有孩子节点为止，再来看它的右孩子，如果都没有的话就弹出元素
# 从栈中弹出元素的条件：指针指向的节点没有左右孩子
class Solution:
    def inorderTraversal(self,root:TreeNode)-> list[int]:
        if not root:
            return []
        stack=[] # 不能提前将root加入
        result=[] # 用于存储结果
        cur=root # 指针，遍历二叉树的元素
        i=1
        while cur or stack:
            # 先迭代访问最底层的左子数节点
            print(f'==========第{i}次遍历==========')
            if cur:
                print(f"访问节点: {cur.val}")
                stack.append(cur) # 将元素入栈
                print(f"结果集的元素:{result}")
                cur=cur.left
            # 到达最左节点后处理栈顶节点
            else:
                cur=stack.pop()
                print(f"弹出节点: {cur.val}")
                result.append(cur.val)
                print(f"结果集的元素:{result}")
                # 取栈顶元素右节点
                cur=cur.right
                if cur:
                    print(f"[变换]访问节点: {cur.val}")
            i+=1
        return result
# 节点4回退到节点2是通过cur=cur.right来实现的，因为cur指向4的时候，4没有右节点，所以后面cur=stack.pop的时候会弹出中间节点2
# 测试代码
if __name__ == "__main__":
    # 创建一个示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 调用中序遍历方法
    solution = Solution()
    inorder_result = solution.inorderTraversal(root)
    print(inorder_result)  # 输出应该是 [4, 2, 5, 1, 3]

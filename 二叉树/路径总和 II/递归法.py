# 递归法
# 分析：
# 1. 确定递归函数的参数和返回类型：
# 参数：二叉树的根节点、计数器（计数器用来计算二叉树的边之和是否正好是目标和）
# 返回值：
# （1）如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（本题的情况）
# （2）如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。
# （3）如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。

# 时间复杂度：O(N*H)
# 1. 树的遍历：函数 traversal 使用的是前序遍历（pre-order traversal），即每个节点会被访问一次，时间复杂度是 O(N)，其中 N 是二叉树中节点的数量。
# 2. 结果路径的存储：
# （1）对于每一条路径，代码会将路径的副本（self.path[:]）添加到 self.result 中。
# （2）在最坏的情况下，树是一颗满二叉树（每个非叶子节点有两个孩子），那么叶子节点的数量是 O(N/2)，每条路径的长度是 O(H)，其中 H 是树的高度。
# （3）在最坏的情况下，树是一颗满二叉树（每个非叶子节点有两个孩子），那么叶子节点的数量是 O(N/2)，每条路径的长度是 O(H)，其中 H 是树的高度。
# 综上，时间复杂度为O(N+N*H)
# 最坏情况下为链表时，H为N，那么这时候为O(N^2)；最好情况下，为平衡二叉树，这时候H为logN，那么为O(NlogN)

# 空间复杂度：O(H+N*H)
# 1. 递归栈空间：函数 traversal 是递归调用，最大递归深度等于树的高度 H，因此递归栈空间的复杂度是 O(H)。
# 2. 路径存储空间
# （1）self.path 存储当前路径，最多需要 O(H) 的空间。
# （2）self.result 最终会存储所有的路径。在最坏的情况下，树是一棵满二叉树，可能有 O(N/2) 条路径，每条路径的长度为 O(H)，因此 self.result 的存储空间复杂度为 O(N * H)。
# 对于平衡树，H=logN，这时候复杂度为O(NlogN)；对于退化成链表的树，H=N，那么复杂度为O(N^2)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result=[] # 结果集
        self.path=[] # 路径
    
    def traversal(self,cur,count):
        if not cur.left and not cur.right and count==0: # 遇到叶子结点，并且这条路径之和为targetSum
            self.result.append(self.path[:]) 
            return
        
        if not cur.left and not cur.right: # 遇到叶子结点
            return 
        
        if cur.left: # 左
            self.path.append(cur.left.val)
            count-=cur.left.val # 递归的前置准备
            self.traversal(cur.left,count) # 递归
            count+=cur.left.val # 回溯
            self.path.pop() # 回溯
        
        if cur.right:
            self.path.append(cur.right.val)
            count-=cur.right.val
            self.traversal(cur.right,count) # 递归
            count+=cur.right.val # 回溯
            self.path.pop() # 回溯
        
        return

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return self.result
        self.path.append(root.val) # 把根节点放进路径
        self.traversal(root,targetSum-root.val)
        return self.result        
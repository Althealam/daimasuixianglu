# 方法：递归法+回溯
# 路径：根节点到叶子结点的路径
# 分析：使用前序遍历，这样才会出现父结点指向孩子节点，这样才能输出从根节点到叶子结点的路径
# 1. 递归函数参数及返回值：传入根节点，记录每一条路径的path，和存放结果集的result
# 2. 确定递归终止条件：找到叶子结点--左右孩子都为空
# 3. 确定单层递归逻辑：前序遍历，需要先处理中结点，中结点就是我们要记录路径上的结点，先放到path中，然后再是递归和回溯
# 时间复杂度：最坏情况下为O(n^2)（树为链式结构），最佳情况下为O(nlogn)（树为平衡二叉树）
# 1. 每个节点访问一次：traversal会对每个节点访问一次（先将节点加入到path列表，然后再递归到左右子节点）
# 2. 路径的生成：在到达叶子节点时，需要将当前路径转换为字符串并加入result。对于一个叶子节点，路径的长度等于树的高度 h。在最坏情况下（树是链式结构），每条路径的长度为 n。因此，对于每个叶子节点，将路径拼接成字符串的时间复杂度为 O(h)。
# 3. 叶子节点的数量：在一棵满二叉树中，叶子节点的数量大约为总节点数的一半，也就是 O(n/2)。
# 最坏情况下每条路径生成字符串的时间复杂度为 O(h)，而叶子节点数量为 O(n/2)，因此拼接所有路径的时间复杂度为 O(n * h)。
# 空间复杂度：最坏情况下O(n^2)，最佳情况下O(nlogn)
# 1. 递归调用栈：递归的深度和树的高度h有关，最坏情况下为n（链式结构），最优情况下为logn
# 2. path列表的空间：path列表用来存储当前路径，它的长度最大为树的高度h，因此 占用空间为O(h)
# 3. result列表的空间：result列表存储了从根到叶子结点的所有路径，最坏情况下，每条路径的长度为h，并且有n/2个叶子结点，因此result的空间复杂度为O(n*h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self,cur,path,result):
        path.append(cur.val) # 中
        if not cur.left and not cur.right: # 到达叶子结点
            sPath='->'.join(map(str,path)) # 路径转换为用->分隔的字符串
            result.append(sPath)
            return
        if cur.left: # 左
            self.traversal(cur.left,path,result)
            path.pop() # 回溯
        if cur.right: # 右
            self.traversal(cur.right,path,result)
            path.pop()

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result=[]
        path=[]
        if not root:
            return result
        self.traversal(root,path,result)
        return result
    

        
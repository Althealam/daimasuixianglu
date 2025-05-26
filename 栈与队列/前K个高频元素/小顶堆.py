# 堆就是利用完全二叉树的结构来维护一维数组
# 小顶堆：每个节点的值都小于或者等于其父节点的值
# 一般的topk问题可以用大/小顶堆来实现，如果是小顶堆则是求最小的K个

# 时间复杂度：O(n)
def build_min_heap(arr):
    """给定数组构造小顶堆（通过调用函数从非叶子节点开始向前调整，保证每个子树都是小顶堆）"""
    n = len(arr)
    
    # 从最后一个非叶子节点开始向前调整
    # 在完全二叉树中，索引大于等于n//2的节点都是叶子节点，不需要调整
    for i in range(n//2 - 1, -1, -1):  # 最后一个非叶子节点的索引是n//2-1
        min_heapify(arr, i, n)
    
    return arr

def min_heapify(arr, index, heap_size):
    """向下调整节点i，维护小顶堆性质（确保以该节点为根的子树满足小顶堆性质）"""
    left = 2 * index + 1  # 左节点
    right = 2 * index + 2  # 右节点
    smallest = index  # 当前最小值的索引
    
    if left < heap_size and arr[left] < arr[smallest]:  # 调整左子节点和该父节点
        smallest = left
    if right < heap_size and arr[right] < arr[smallest]:  # 调整右子节点和该父节点
        smallest = right
    
    if smallest != index:  # 当前遍历的节点值是index，最小节点是smallest，需要交换位置并维护其对应的子树
        arr[index], arr[smallest] = arr[smallest], arr[index]
        min_heapify(arr, smallest, heap_size)  # 递归调整子树
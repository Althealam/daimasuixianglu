# 时间复杂度：O(n)
def build_max_heap(arr):
    """给定数组构造大顶堆（通过调用函数从非叶子节点开始向前调整，保证每个子树都是大顶堆）"""
    n=len(arr)

    # 从最后一个非叶子节点开始向前调整
    # 比如数组[3,5,1,2,6]，构造二叉树后最后一个非叶子节点是5，其索引为1，也就是5//2-1
    # 在完全二叉树中，索引大于等于n//2的节点都是叶子节点，不需要调整
    for i in range(n//2-1, -1, -1): # 最后一个非叶子节点的索引是n//2-1
        max_heapify(arr, i, n)
    
    return arr

def max_heapify(arr, index, heap_size):
    """向下调整节点i，维护大顶堆性质（确保以该节点为根的子树满足大顶堆性质）"""
    left=2*index+1 # 左节点
    right=2*index+2 # 右节点
    largest=index # 需要维护的节点值
    if left<heap_size and arr[left]>arr[largest]: # 调整左子节点和该父节点
        largest=left
    if right<heap_size and arr[right]>arr[largest]: # 调整右子节点和该父节点
        largest=right
    if largest!=index:
        arr[index], arr[largest]=arr[largest], arr[index]
        max_heapify(arr, largest, heap_size) # 递归调整子树

arr=[4,10,3,5,1]
heap=build_max_heap(arr)
print(heap)
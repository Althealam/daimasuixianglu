# 最大堆可以让数组变成递增的，而最小堆可以让数组变成递减的。

# 时间复杂度：O(nlogn) 堆排序的时间复杂度为O(nlogn) 构建最大堆的时间复杂度为O(n) 每次调整堆的时间为O(logn)
# 空间复杂度：原地排序算法，空间复杂度为O(1)

def min_heapify(arr, n, i):
    # 当前节点为最小值的索引
    smallest = i
    # 当前节点的左子节点的索引
    left = 2 * i + 1
    # 当前节点的右子节点的索引
    right = 2 * i + 2

    # 如果左子节点存在并且左子节点的值小于当前最小值节点的值
    if left < n and arr[left] < arr[smallest]:
        # 更新最小值节点的索引
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # 如果最小值节点不是当前根节点，则交换它们，并继续调整子树
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)

    # 构建最小堆
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # 一个个交换元素
    result = []
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        result.append(arr.pop())
        if arr:
            min_heapify(arr, len(arr), 0)

    result.reverse()
    return result

# 测试代码
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = min_heap_sort(arr)
print("最小堆排序后的数组:", sorted_arr)
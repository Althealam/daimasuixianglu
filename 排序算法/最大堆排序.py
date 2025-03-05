# 时间复杂度：O(nlogn) 堆排序的时间复杂度为O(nlogn) 构建最大堆的时间复杂度为O(n) 每次调整堆的时间为O(logn)
# 空间复杂度：原地排序算法，空间复杂度为O(1)

# 1. heapify函数：
# （1）将以索引i为根节点的子树调整为最大堆
# （2）首先找出根节点、左子节点和右子节点中的最大值节点的索引largest
# （3）如果largest不等于i，就交换根节点和largest的值，并且调用heapify继续调整以largest为根节点的树
# 2. heap_sort函数：
# （1）构建最大堆：从最后一个非叶子节点开始，依次调用heapify函数，将整个数组调整为最大堆
# （2）一个个交换元素，将堆顶元素（最大值）与当前未排序部分的最后一个元素交换，然后排除已排序的元素，重新调整堆，直到整个数组有序

def heapify(arr, n, i):
    """ 
    此函数用于将以索引 i 为根节点的子树调整为最大堆
    :param arr: 待调整的数组
    :param n: 当前堆的大小
    :param i: 当前要调整的节点索引
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 检查左子节点是否存在且大于根节点
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 检查右子节点是否存在且大于当前最大值节点
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值节点不是当前根节点，则交换它们，并继续调整子树
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    堆排序主函数
    :param arr: 待排序的数组
    :return: 排序好的数组
    """
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 将堆顶元素（最大值）与当前未排序部分的最后一个元素交换
        heapify(arr, i, 0)  # 重新调整堆，排除已排序的元素

    return arr

# 测试代码
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("排序后的数组:", sorted_arr)
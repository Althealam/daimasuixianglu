# 时间复杂度：O(nlogn) 堆排序的时间复杂度为O(nlogn) 构建最大堆的时间复杂度为O(n) 每次调整堆的时间为O(logn)
# 空间复杂度：原地排序算法，空间复杂度为O(1)
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

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
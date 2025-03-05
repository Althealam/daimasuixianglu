# 时间复杂度：O(nlogn)，最坏情况下为O(n^2)
# 空间复杂度：O(logn)
def partition(arr, low, high):
    pivot=arr[high] # 选择最右边的元素作为基准
    i=low-1
    for j in range(low, high):
        if arr[j]<=pivot:
            i=i+1
            # 交换元素
            arr[i], arr[j]=arr[j], arr[i]
    # 将基准元素放到正确的位置
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1

def quick_sort_non_recursive(arr):
    if len(arr)<=1:
        return arr
    # 初始化栈，栈中存储待排序子数组的起始和结束索引
    stack=[]
    # 初始时将整个数组的起始位置和结束位置索引入栈
    stack.append((0, len(arr)-1))

    while stack:
        # 从栈中弹出一个待排序子数组的起始和结束索引
        low, high=stack.pop()
        # 进行分区操作，获取基准元素的最终位置
        pivot_index=partition(arr,low,high)

        # 如果基准元素左边还有元素，将左边子数组的起始和结束索引入栈
        if pivot_index-1>low:
            stack.append((low, pivot_index-1))
        # 如果基准元素右边还有元素，将右边子数组的起始和结束索引入栈
        if pivot_index+1<high:
            stack.append((pivot_index+1, high))
        
    return arr
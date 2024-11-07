# 快速排序
# 思想：快速排序选择一个基准元素，将数组分为两部分：小于基准的和大于基准的，然后递归排序两部分

# 时间复杂度：
# 快速排序的时间复杂度依赖于pivot如何分割数组。
# 1. 最好情况：如果基准元素每次都能把数组大致平分成两个相同大小的子数组，那么每次递归调用处理的子数组大小会减半
# 每一轮的工作量是O(n)（每个元素都需要与基准元素比较一次），递归深度为P(logn)（每次都分成两个相等的部分）-- 总时间复杂度为O(nlogn)
# 2. 最坏情况：如果每次选择的基准元素是数组中的最小或最大元素（例如，如果数组已经是有序的或者是逆序的），则数组无法有效分割。
# 递归深度为O(n)，每一轮比较多工作量为O(n)，那么此时的时间复杂度为O(n^2)

# 空间复杂度：主要来自于递归调用和存储子数组的空间需求。
# 1. 递归调用栈空间：每次递归调用都会栈上保存当前函数的状态。如果分割是均匀的，每次分成两个部分，递归深度为O(logn)，因此递归调用栈的空间复杂度为O(logn)
# 2. 子数组的空间需求：快速排序是通过创建新的子数组left, middle, right来实现的，这些新数组大小等于原数组的大小
# 每一次递归都会消耗O(n)的空间来存储left, middle, right数组
# 综上，总空间复杂度为O(n)

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

arr=[5,3,8,4,2]
quick_sort(arr)
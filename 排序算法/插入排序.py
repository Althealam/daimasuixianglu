# 插入排序
# 思想：插入排序通过将每个新元素插入到已经有序的部分，使整个数组保持有序。
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i] # 用来保存arr[i]的值
        j=i-1
        # 这段代码主要是判断新元素与已排序部分的元素的大小关系，如果是大于的话，相当于新元素需要插入到已排序的元素当中去
        # 把新元素插入到已排序部分中：1. 利用后面的元素覆盖前面的元素 2. 找到要插入的位置后，用key覆盖该元素的值
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[5,3,8,4,2]
insertion_sort(arr)
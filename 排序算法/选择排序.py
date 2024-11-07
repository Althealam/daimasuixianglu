# 选择排序
# 基本思想：每次从未排序的部分选择最小的元素，然后将其放到已排序部分的末尾
# 步骤：1. 从未排序部分中选择最小的元素，然后将这个最小元素放到已排序部分的末尾 2. 在剩下的未排序部分继续进行相同的操作
# 时间复杂度：O(n^2)
# 外层循环：从第一个元素开始，一直到倒数第一个元素
# 内层循环：第一次内层循环遍历整个数组n次，第二次内层循环遍历整个数组n-1次，总共是(n-1)+(n-2)+...+1=n(n-1)/2次
# 空间复杂度：O(1)
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i # 用来记录未排序的部分的最小的元素的下标
        # 这段遍历相当于找未排序部分的最小的元素的下标min_idx
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        # 这段代码相当于将未排序部分的最小元素放到已排序部分的开头
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

arr=[5,3,8,4,2]
selection_sort(arr)
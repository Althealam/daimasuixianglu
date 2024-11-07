# 归并排序
# 思想：归并排序将数组不断分割成更小的部分，排序并合并这些部分，最终得到有序数组。

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left(i)<right[j]
        result.append(left[i])
        i+=1
    else:
        result.append(right[j])
        j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 思路：需要x**y>y**x，也就是x/log(x)<y/log(y)
# 求出数组x_array和y_array，然后找到x_array中小于y_array的数量即可

# 时间复杂度：O(nlogn+mlogm)
# 1. 计算变换后的数组：O(n+m)
# 2. 排序：O(nlogn+mlogm)
# 3. 双指针遍历：O(n+m)
# 空间复杂度：利用O(n+m)的空间来存储变换后的数组

import math

def count_pairs(arr1, arr2):
    x_transformed=[x/math.log(x) if x>1 else float('-inf') for x in arr1]
    y_transformed=[y/math.log(y) if y>1 else float('-inf') for y in arr2]

    x_transformed.sort()
    y_transformed.sort()

    count=0 # 计算符合条件的元素对的个数
    j=0 # 遍历y_transformed的指针

    # 遍历排序过的x_transformed数组
    for x in x_transformed:
        # 说明此时从当前x到x_transformed数组的末尾的元素都满足与y_transformed[j]构成元素对
        # 从x到x_transformed数组的末尾的元素个数为len(x_transformed)-(x_transformed.index(x))
        while j<len(y_transformed) and x<y_transformed[j]:
            count+=len(x_transformed)-(x_transformed.index(x))
            j+=1 # 判断下一个j元素
    return count


arr1=[2,4]
arr2=[3,5]
print(count_pairs(arr1, arr2))
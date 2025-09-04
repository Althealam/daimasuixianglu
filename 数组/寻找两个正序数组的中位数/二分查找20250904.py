# 在两个有序数组中，查找第k小的数，其中k=(m+n)//2
# 1. 如果m+n为奇数，那么返回第k小的数
# 2. 如果m+n为偶数，则返回第k小的数和第k+1小的数的平均值
# 思路：在两个数组中找到合适的分割线，使得分割线左边的所有元素都小于右边的所有元素，并且左右两边的元素数量相等或者左边多一个
# 1. 在较短的数组上进行二分查找
# 2. 对于每个可能的分割位置，计算另一个数组的对应分割位置
# 2. 检查分割线是否满足条件（左边最大值<=右边最小值）

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1是较短的数组
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m+n+1)//2 # 在较短的数组上进行二分查找
        # imin, imax是nums1的搜索区间，half_len是左半部分的总长度

        while imin<=imax:
            # 二分查找分割线
            i = (imin+imax)//2 # nums1的分割点
            j = half_len-i # nums2的分割点
            # 左边为nums1[0..i-1]+nums2[0..j-1]
            # 右边为nums1[i..m-1]+nums2[j..n-1]

            # 处理边界情况
            if i<m and nums2[j-1]>nums1[i]: # nums1[i]需要放到右边，因此i太小了
                # i太小，需要增大
                imin = i+1
            elif i>0 and nums1[i-1]>nums2[j]: # nums1[i]需要放到左边，因此i太大了
                # i太大，需要减小
                imax = i-1
            else:
                # 找到合适的分割线，处理中位数计算
                if i==0: # nums1没有左半部分
                    max_of_left = nums2[j-1]
                elif j==0: # nums2没有左半部分
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                # 如果总数是奇数，直接返回左半部分最大值
                if (m+n)%2==1:
                    return max_of_left
                
                # 计算右半部分最小值
                if i==m:
                    min_of_right = nums2[j]
                elif j==n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(num1[i], num2[j])
                
                return (max_of_left+min_of_right)/2.0 # 偶数返回平均值
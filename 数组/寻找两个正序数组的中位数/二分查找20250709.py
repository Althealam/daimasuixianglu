# 本质：在两个有序数组中，查找第k小的数，其中k=(m+n)//2
# （1）如果m+n为奇数，则返回第k小的数
# （2）如果m+n为偶数，则返回第k小的数和第k+1小的数的平均值

# 注意：如果直接合并两个有序数组后再去寻找中位数，那么时间复杂度为O(m+n)，不符合题目含义

# 核心思想：二分查找分割线：将问题转化为在两个数组中寻找合适的分割线，使得分割线左边的所有元素都小于等于右边的所有元素，并且左右两边的元素数量相等或者左边多一个

# 在较短的数组上二分查找，对于每个可能的分割位置，计算另一个数组的对应分割位置，检查分割线是否满足条件（左边最大值<=右边最小值），根据比较结果调整二分查找的范围

# nums1=[a1,a2,a3,...,an] nums2=[b1,b2,b3,...,bn]
# nums1[:left1], nums2[:left2]|nums1[left1:], nums2[left2:]
# 只要保证左右两边个数相同，中位数就在|这个边界的旁边产生

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1 # 让nums2为长度最长的数组

        m, n = len(nums1), len(nums2)
        a = [-inf]+nums1+[inf]
        b = [-inf]+nums2+[inf]

        # 枚举nums1有i个数在第一组
        # 枚举nums2有j=(m+n+1)//2-i个数在第二组
        i, j = 0, (m+n+1)//2
        while True:
            if a[i]<=b[j+1] and a[i+1]>b[j]:
                max1 = max(a[i], b[j]) # 第一组的最大值
                min2 = min(a[i+1], b[j+1]) # 第二组的最小值
                return max1 if (m+n)%2 else (max1+min2)/2
            # 继续枚举
            i+=1 
            j-=1
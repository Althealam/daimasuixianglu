# 思路：
# 1. 遍历nums1和nums2，用dict记录两个数组的元素分别相加的和以及其出现的次数，并记录到dict中
# 2. 遍历nums3和nums4，判断-nums3[i]-nums4[j]有没有出现在dict中，如果有的话，则用count加上对应的dict的value值

# 时间复杂度：O(mn+pq)，其中m,n,p,q分别是num1,nums2,nums3,nums4的长度
# 空间复杂度：O(mn)，最坏的情况下，两数之和可能都不相同

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash=dict()
        # 1. 统计nums1和nums2中的元素相加之和出现的次数
        for index1, value1 in enumerate(nums1):
            for index2, value2 in enumerate(nums2):
                if value1+value2 in hash:
                    hash[value1+value2]+=1
                else:
                    hash[value1+value2]=1
        count=0 # 用来记录四数相加之和出现的次数
        # 2. 判断-nums3[i]-nums4[j]是否在hash中出现过
        for index1, value1 in enumerate(nums3):
            for index2, value2 in enumerate(nums4):
                x=-value1-value2
                if x in hash:
                    count+=hash[x]
        return count


        
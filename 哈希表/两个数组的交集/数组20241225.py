# 思路：统计nums1和nums2中各个元素出现的次数，并且用hash表存储
# 同时遍历两个hash表，如果出现对应的value1*value2>0，就说明这个元素是两个数组都出现的元素

# 时间复杂度：O(m+n)，m是nums1的长度，n是nums2的长度
# 空间复杂度：O(1)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts1=[0]*1001
        counts2=[0]*1001
        result=[]
        for i in range(len(nums1)):
            counts1[nums1[i]]+=1
        for i in range(len(nums2)):
            counts2[nums2[i]]+=1
        for k in range(1001):
            if counts1[k]*counts2[k]>0:
                result.append(k)
        return result


        
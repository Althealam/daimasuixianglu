# 使用数组
# 时间复杂度：O(n+m) n为nums1数组的长度，m为nums2数组的长度
# 空间复杂度：O(1) 利用两个长度为1001的列表count1和count2来存储计数
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1=[0]*1001 # 初始化一个长度为1001的列表count1，用于统计nums1中每个元素的出现次数
        count2=[0]*1001 # 初始化一个长度为1001的列表count2，用于统计nums2中每个元素的出现次数
        result=[] # 用于存储最终的交集结果
        for i in range(len(nums1)):
            count1[nums1[i]]+=1 # 对于nums1中的每个元素，将其在count1列表中对应的索引的值加1，从而统计每个元素的出现次数
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001): # 遍历count1和count2列表中对应索引的值的乘积是否大于0，如果大于0说明两个数组中都出现了索引为k的元素
            if count1[k]*count2[k]>0:
                result.append(k)
        return result
# 思路：二分法（左闭右闭）
# 1. 定义一个left和right，left从最左边出发，right从最右边出发；定义mid=(left+right)/2
# 2. 判断mid和target的大小
#（1）nums[mid]<target：target在[mid+1,right]，更新left和right
#（2）nums[mid]>target：target在[left,mid-1]，更新left和right
#（3）nums[mid]=target：记录mid的位置，返回该下标
# 终止条件：left=right（一直没找到下标），返回-1


# 时间复杂度：O(log2n)
# 假设有序列表nums的长度为n，循环次数为k，那么存在这样的关系：n*(1/2)^k<=1-->k>=log2n
# 最坏情况是，一直查找区间缩小为空都没有找到目标值。初始时查找区间长度为n，经过第一次循环后区间长度变为n/2，第二次循环后变为n/4，以此类推。直到最后查找区间长度变为1。
# 空间复杂度：O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right=0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return -1



        
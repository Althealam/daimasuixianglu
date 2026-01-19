class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0 # 不重复数组的最后一个位置
        fast=1 # 遍历数组，寻找新的元素
        while fast<=len(nums)-1:
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return slow+1
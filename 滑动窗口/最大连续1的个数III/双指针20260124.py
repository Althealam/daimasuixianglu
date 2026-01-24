# 找到最长的连续子数组，其中0的数量小于等于k
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        max_length = 0
        for right, c in enumerate(nums):
            if c==0:
                count+=1
            # 移动滑动窗口的条件是子数组内的0的出现次数大于K
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            # 更新子字符串的长度
            max_length = max(max_length, right-left+1)
        return max_length
                
            
        
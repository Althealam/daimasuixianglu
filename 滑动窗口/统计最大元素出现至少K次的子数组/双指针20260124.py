class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0 # 最大元素的出现次数
        max_num = max(nums) # 最大元素
        left = 0
        ans = 0 # 最大元素出现次数超过K的子数组的数量
        for right in range(len(nums)):
            # 遇到了一个最大元素
            if nums[right]==max_num:
                count+=1
            # 最大元素的出现次数等于K
            # 移动滑动窗口直到最大元素的出现次数小于K
            while count==k:
                if nums[left]==max_num:
                    count-=1
                left+=1
            ans+=left
        return ans

            

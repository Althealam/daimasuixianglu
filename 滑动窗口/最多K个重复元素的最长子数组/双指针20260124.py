class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        left = 0
        max_length = 0
        for right, c in enumerate(nums):
            cnt[c]+=1
            while cnt[c]>k:
                cnt[nums[left]]-=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length
            
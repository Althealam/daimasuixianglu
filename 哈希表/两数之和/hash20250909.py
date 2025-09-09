class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target-num in hash_map:
                return [i, hash_map[target-num]]
            else:
                hash_map[num]=i        
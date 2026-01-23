class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map_num = {}
        for i in range(len(nums)):
            if target-nums[i] in hash_map_num:
                return [i, hash_map_num[target-nums[i]]]
            else:
                hash_map_num[nums[i]]=i
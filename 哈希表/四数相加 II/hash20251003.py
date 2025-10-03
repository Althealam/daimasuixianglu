class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        hash_map = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 not in hash_map:
                    hash_map[num1+num2]=1
                else:
                    hash_map[num1+num2]+=1
        
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in hash_map:
                    ans+=hash_map[-(num3+num4)]
        return ans
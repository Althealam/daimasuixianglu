class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt_nums1 = Counter(nums1)
        ans = []
        for num in nums2:
            if num in cnt_nums1 and cnt_nums1[num]>0:
                cnt_nums1[num]-=1
                ans.append(num)
        return ans
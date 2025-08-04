class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map_nums1 = [0]*1001
        hash_map_nums2 = [0]*1001
        ans = []
        for num1 in nums1:
            hash_map_nums1[num1]+=1
        for num2 in nums2:
            hash_map_nums2[num2]+=1
        for i in range(1001):
            if hash_map_nums1[i]*hash_map_nums2[i]>0:
                ans.append(i)
        return ans
        


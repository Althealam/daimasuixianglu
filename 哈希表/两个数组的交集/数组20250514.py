class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict=[0]*1001
        nums2_dict=[0]*1001
        for num in nums1:
            nums1_dict[num]+=1
        for num in nums2:
            nums2_dict[num]+=1
        ans=[]
        for i in range(1001):
            if nums1_dict[i]*nums2_dict[i]>0:
                ans.append(i)
        return ans

        
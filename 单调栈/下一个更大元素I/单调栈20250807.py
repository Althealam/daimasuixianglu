# 1. 单调栈中存储nums1中还没有找到下一个更大元素i的元素下标
# 2. 定义一个map存储nums1的下标和值的map 
# 3. 遍历nums2，找到每个元素的下一个更大元素
# 4. 利用map还原nums1的情况
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        st = []
        hash_map = {x:i for i, x in enumerate(nums1)} # i是索引，x是对应的值
        for i in range(len(nums2)):
            while len(st)!=0 and nums2[i]>st[-1]:
                if st[-1] in nums1:
                    ans[hash_map[st[-1]]] = nums2[i]
                st.pop()
            st.append(nums2[i])
        return ans



        
            

        
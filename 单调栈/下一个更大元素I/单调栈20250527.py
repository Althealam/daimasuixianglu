# 思路：
# 1. 定义一个单调栈，栈中存储的是nums2中还没找到答案的元素
# 2. 使用单调栈，找到nums2中每个元素的答案值，如果nums2的元素也在nums1中，则更新nums1该元素的答案值

# 时间复杂度：O(m+n)，其中m是nums1的长度，n是nums2的长度
# 空间复杂度：O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map={x:i for i, x in enumerate(nums1)}
        ans=[-1]*len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]: # 找到了stack[-1]的答案值，为nums2[i]
                j=stack.pop() # 弹出栈顶元素
                if j in map.keys(): # 查看stack[-1是否早nums1中
                    ans[map[j]]=nums2[i] # 如果在的话，则更新stack[-1]的答案值为nums2[i]
            stack.append(nums2[i])
        return ans
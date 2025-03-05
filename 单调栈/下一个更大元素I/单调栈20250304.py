# answer=[-1]*(len(nums1))
# 1. 找到nums2的单调栈左边的第一个更大的元素值：
# (1) if nums2[i]>nums2[stack[-1]]: answer[stack[-1]]=i-stack[-1] stack.pop() stack.append(i)
# (2) if nums2[i]<=nums2[stack[-1]]: stack.append(i)
# 2. 判断nums2的每个元素是否在nums1中存在，存在的话则记录result值，注意这里存储的是元素值，而不是下标差

# 时间复杂度：O(n2) n2是nums2的数组长度
# 空间复杂度：O(n1+n2) n1是nums1的数字长度，n2是nums2的数组长度
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer=[-1]*len(nums2) # 记录nums2的值
        result=[-1]*len(nums1) # 记录nums1的值
        stack=[0]
        for i in range(1, len(nums2)):
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index=nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return result

        
# 分析：需要定义一个和nums1一样大小的数组result来存放结果
# 如果不存在对应位置就输出-1，所以result数组应该全部初始化为-1
# 遍历单调栈：
# 1. T[i]<T[st.top()]: 满足递增栈，直接入栈
# 2. T[i]=T[st.top()]: 直接入栈
# 3. T[i]>T[st.top()]: 找到右边第一个比自己大的元素（判断栈顶元素是否在nums1中出现过，如果出现过，则开始记录结果）

# 时间复杂度：
# 1. 外层循环遍历nums2的所有元素，O(m)（m是nums2的长度）
# 2. 内层循环
# 3. nums1.index()操作：对于每次找到满足条件的nums2[stack[-1]]，利用nums1.index()查找其在nums1中的索引
# 最坏情况下，这种查找操作需要O(n)的时间，其中n是nums1的长度
# 总的时间复杂度为O(m+m*n)=O(m*n)

# 空间复杂度：
# 1. 栈：存储nums2中的元素索引，最坏情况下nums2是单调递减的，栈的大小最多为m
# 2. 结果数组：result的大小为n，与nums1的长度一致
# 总的空间复杂度为O(m+n)

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[-1]*len(nums1)
        stack=[0]
        for i in range(1,len(nums2)):
            # 情况一和情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index=nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()
                stack.append(i)

        return result
        
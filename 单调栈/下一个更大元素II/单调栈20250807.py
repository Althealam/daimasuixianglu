# 1. 将nums变成两个子数组拼接
# 2. 遍历new_nums，定义单调栈，栈中存储没有找到下一个更大元素的元素下标
# 3. 如果当前遍历的new_nums[i]大于new_nums[st[-1]]（也就是比栈顶元素值大），那么弹出栈顶元素，更新栈顶元素的答案值

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        new_nums = nums*2
        ans = [-1]*len(nums)
        for i in range(len(new_nums)):
            while len(st)!=0 and new_nums[i]>new_nums[st[-1]]:
                ans[st[-1]%len(nums)] = new_nums[i]
                st.pop()
            st.append(i)
        return ans      
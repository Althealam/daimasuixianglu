# 单调栈的使用方法：一维数组，想要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，此时可以用单调栈
# 单调栈的原理：用一个栈来记录我们遍历过的元素，并且单调栈里存放的是元素的下标i（否则还要去数组里找下标，很麻烦）
# 单调栈的递增递减顺序指的是从栈口到栈底的顺序
# 如果遍历到nums的元素nums[i]的值是大于栈的栈顶元素的，那么answer[i]=i-栈顶元素的下标，否则的话将nums[i]入栈

# 情况1：temperatures[i]>temperatures[stack[-1]]: answer[i]=i-stack[-1] stack.pop() stack.append(i)
# 情况2：temperatures[i]<=temperatures[stack[-1]]: stack.append(i)

# 时间复杂度：O(n)
# 空间复杂度：O(n)
 
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        stack=[0] # 先入栈temperatures的第一个元素
        for i in range(1, len(temperatures)): # 情况2
            if temperatures[i]<=temperatures[stack[-1]]: # stack[-1]表示的是栈顶元素
                stack.append(i)
            else: # 情况1
                while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return answer


        
# 分析：找元素右边第一个比他大的元素距离该元素的位置
# 什么时候用单调栈：一维数组，想要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置（单调栈的本质是空间换时间）
# 单调栈里存放的元素是什么：元素的下标i
# 单调栈内元素的顺序（从栈头到栈底）：
# （1）单调栈是递增的：求该元素右边第一个比他大的元素
# （2）单调栈是递减的：求该元素右边第一个比他小的元素
# 单调栈是用于存放遍历过的元素的，可以用于进行对比
# 单调栈的来源：比较当前遍历的元素与栈口的元素的大小
# （1）如果大于的话就弹出栈顶的元素，加入当前遍历的元素
# （2）如果小于的话，就直接将当前遍历的元素加入单调栈
# （3）如果相等的话，也加入栈里

# 时间复杂度：
# 1. 主循环：O(n)
# 2. 内循环：在最坏情况下，栈中的每个元素只会被访问两次：每个元素最多被压入栈一次；每个元素最多被弹出栈一次
# 总的时间复杂度为O(n)
# 空间复杂度：
# 1. 使用了一个stack存储元素的索引，最坏情况下所有元素都会依次入栈，栈的大小最多为n
# 2. 使用了一个answer数组，占用O(n)的空间
# 总的空间复杂度为O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        stack=[0]
        for i in range(1,len(temperatures)):
            # 情况一和情况二
            # 目前遍历的元素为temperatures[i]，栈顶的元素为temperatures[stack[-1]]
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return answer

        
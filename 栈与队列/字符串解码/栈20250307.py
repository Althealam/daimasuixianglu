# 时间复杂度：O(n)
# 1. 遍历字符串：for循环遍历字符串s中的每个字符，循环次数为n
# 2. 字符处理：
# （1）遇到[时，将当前的重复次数multi和当前结果res压入栈中 O(1)
# （2）遇到]时，从栈中弹出元素，并进行字符串拼接和重复操作。
# （3）遇到数字字符时，更新multi的值 O(1)
# （4）遇到其他字符时，将其添加到res中 O(1)

# 空间复杂度：O(n)
# 1. 栈的空间：栈的深度可能达到输入字符串中嵌套方括号的最大深度。
# 假设输入字符串中嵌套方括号的最大深度为m，则栈的空间复杂度为O(m)
# 2. 结果字符串的空间：最坏情况下，解码后的字符串长度可能达到O(n)，其中n是输入字符串的长度。


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[] # 存储每一层嵌套的重复次数multi和当前已经解码好得字符串res（每个元素是一个包含两个元素的列表 [multi, res]）
        res="" # 存储当前正在构建的解码后的字符串
        multi=0 # 用于记录当前层方括号前面的重复次数
        for c in s:
            # 遇到[代表即将进入一个新的嵌套层
            if c=='[':
                stack.append([multi, res])
                res, multi="", 0 # 为处理新的嵌套层做准备
            # 遇到]代表嵌套层处理完毕，需要从栈中弹出上一层的信息
            elif c==']':
                cur_multi, last_res=stack.pop() # 上一层的重复次数为cur_multi和已经解码好的字符串last_res
                res=last_res+cur_multi*res # 将上一层的字符串last_res和当前层重复cur_multi次后的字符串拼接起来，更新res
            # 遇到字符c是数字字符，说明它是当前层方括号前面的重复次数的一部分
            elif '0'<=c<='9': 
                multi=multi*10+int(c) # 更新multi的值
            else:
                res+=c
        return res
    
s="3[a2[c]]"
solution=Solution()
result=solution.decodeString(s)
print(result)
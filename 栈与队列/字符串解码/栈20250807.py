# 分析：
# 1. 定义栈，遍历字符串
# 2. 出现数字，则累乘计算值
# 3. 出现[表示前置子串和重复次数遍历完成，将变量res和k的值暂时存在栈中
# 4. 出现]表示括号内的重复子串遍历完成，需要展开
# 5. 出现字母则直接拼接

# 思路：
# 1. stack：栈，用来保存上一层的字符串和当前括号的重复次数
# 2. res：当前正在处理的字符串
# 3. k：当前括号的重复次数
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = "" # 方括号内的元素
        k = 0 # 方括号内的元素的出现次数
        for i in range(len(s)):
            print(i, s[i])
            # 出现数字字符则累乘计算值
            if "0"<=s[i]<="9":
                k = k*10+int(s[i])
            # 出现[表示前置子串和重复次数遍历完成，为了解析和存储括号内可能出现的新字符串和数值，将变量res和k的值暂时存在栈中
            elif s[i]=='[':
                stack.append((res, k))
                res, k = "", 0 # 入栈后要将res和k清空
            # 出现]表示括号内的重复子串遍历完成，需要展开
            elif s[i] == ']': 
                last_res, cur_k = stack.pop()
                res = last_res+cur_k*res
            # 出现字母则直接拼接
            else:
                res +=s[i]
            print(stack)
        return res
    
s = "3[a]2[bc]"
sol = Solution()
res = sol.decodeString(s)
print(res)
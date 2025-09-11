class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        k = 0
        for i in range(len(s)):
            # 出现数字则计算值
            if "0"<=s[i]<="9":
                k = k*10+int(s[i])
            # 前置子串和重复次数遍历完成
            elif s[i]=='[':
                stack.append((res, k))
                res, k = "", 0
            # 括号内的重复子串遍历完成，需要展开
            elif s[i]==']':
                last_res, cur_k = stack.pop()
                res = last_res+cur_k*res
            # 出现字母
            else:
                res+=s[i]
        return res
        
        
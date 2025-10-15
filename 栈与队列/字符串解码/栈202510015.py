class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        k = 0
        for i in range(len(s)):
            # 出现数字则更新字符重复的次数
            if "0"<=s[i]<="9":
                k = k*10+int(s[i]) # 需要乘上10以防万一这个数字是大于等于10的
            elif s[i]=='[': # 前置子串和重复次数遍历完成
                stack.append((res, k)) # res对应当前的字符串（需要进行重复的字符串），k对应字符重复的次数
                res, k = "", 0
            elif s[i]==']': # 括号内的重复字符串已经遍历完成，需要展开
                last_res, cur_k = stack.pop()
                res = last_res+cur_k*res 
            else:
                res+=s[i] # 将字母加入到res中
        return res
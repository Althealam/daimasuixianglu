class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 如果s为空串，则直接返回True
        if not s:
            return True
        
        i = 0 # 遍历s的位置
        # 遍历t的字符c，判断是否和s[i]匹配，如果匹配的话则i+=1
        for c in t:
            if s[i]==c:
                i+=1 # 开始判断s的下一个字符
                if i==len(s): # 已经遍历完s了
                    return True
        return False
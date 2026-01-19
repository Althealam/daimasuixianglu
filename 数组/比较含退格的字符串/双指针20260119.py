class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        skip1 = skip2 = 0
        while i>=0 or j>=0:
            # 找到s的下一个有效字符
            while i>=0:
                if s[i]=='#':
                    skip1+=1
                    i-=1
                elif skip1>0:
                    skip1-=1
                    i-=1
                else:
                    break
            
            # 找到t的下一个有效字符
            while j>=0:
                if t[j]=='#':
                    skip2+=1
                    j-=1
                elif skip2>0:
                    skip2-=1
                    j-=1
                else:
                    break
            # 只有一个越界
            if (i<0 and j>=0) or (i>=0 and j<0):
                return False
            # 两个都没有越界
            if i>=0 and j>=0 and s[i]!=t[j]:
                return False
            # 两个都越界了
            if i<0 and j<0:
                return True
            i-=1
            j-=1
        return True

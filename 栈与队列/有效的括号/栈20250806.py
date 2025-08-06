class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(')')
            elif s[i]=='[':
                stack.append(']')
            elif s[i]=='{':
                stack.append('}')
            else:
                if len(stack)==0:
                    return False
                else:
                    node = stack.pop()
                    if node==s[i]:
                        continue
                    else:
                        return False
        return True if len(stack)==0 else False
        
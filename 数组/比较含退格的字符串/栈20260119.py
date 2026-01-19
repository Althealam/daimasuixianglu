class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for st in list(s):
            if st!='#':
                st1.append(st)
            elif st=='#' and len(st1)!=0:
                st1.pop()
        for st in list(t):
            if st!='#':
                st2.append(st)
            elif st=='#' and len(st2)!=0:
                st2.pop()
        return st1==st2
        
# 思路：定义一个set来存储出现过的数字 如果数字重复出现在set中说明就不是快乐数 否则的话一直找到1的情况
class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n not in st:
            st.add(n)
            n = self.get_new_n(n)
            if n==1:
                return  True
        return False
    
    def get_new_n(self, n):
        str_n = str(n)
        list_n = list(str_n)
        ans = 0
        for num in list_n:
            ans+=int(num)**2
        return ans

        
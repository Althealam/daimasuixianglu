class Solution:
    def isHappy(self, n: int) -> bool:
        record=set() # 存储出现过的sum值
        while n not in record:
            record.add(n)
            new_sum=0 # 重新计算的sum值
            n_str=str(n)
            # 计算n_str的sum
            for i in n_str:
                new_sum+=int(i)**2
            if new_sum==1:
                return True
            n=new_sum
        return False
        
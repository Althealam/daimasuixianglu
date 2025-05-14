class Solution:
    def isHappy(self, n: int) -> bool:
        record=[]
        while n not in record:
            record.append(n)
            str_n=str(n)
            new_sum=0
            for i in str_n:
                new_sum+=int(i)**2
            if new_sum==1:
                return True
            n=new_sum
        return False

# 思路：
# 1. 收入是5，直接收下
# 2. 收入是10，消耗一个5，增加一个10
# 3. 收入是20，优先消耗一个10和一个5，否则消耗3个5

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cnt_5=0
        cnt_10=0
        cnt_20=0
        for i in range(len(bills)):
            # 收到5美元
            if bills[i]==5:
                cnt_5+=1 # 直接收下5美元
            # 收到10美元
            if bills[i]==10:
                if cnt_5>0:  # 减去一张5美元，增加一张10美元
                    cnt_5-=1 
                    cnt_10+=1
                else:
                    return False
            # 收到20美元
            if bills[i]==20:
                if cnt_10>=1 and cnt_5>=1: # 减去一张10美元，减去一张10美元，增加一张20美元
                    cnt_10-=1
                    cnt_5-=1
                    cnt_20+=1
                elif cnt_10==0 and cnt_5>=3: # 减去3张5美元
                    cnt_5-=3
                    cnt_20+=1
                else:
                    return False
        return True

        
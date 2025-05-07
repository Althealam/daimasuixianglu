# 思路：
# 1. 用户支付20美元：（1）找10+5 （2）找3*5
# 2. 用户支付10美元：找5
# 3. 用户支付5：手下5
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        twenty=0
        ten=0
        five=0
        for bill in bills:
            if bill==20:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                else:
                    return False
            elif bill==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                five+=1
        return True
        
        
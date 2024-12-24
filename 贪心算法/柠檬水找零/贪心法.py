# 分析：
# 1. 用户支付5: 直接收走
# 2. 用户支付10: 用5找零
# 3. 用户支付20: （1）用5+10找零（2）用5+5+5找零（优先使用第一个策略，因为尽可能拥有5在手上，5可以处理第二个情况）
# 贪心的策略应用于优先使用10找零
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five=0 # 面额为5的数量
        ten=0 # 面额为10的数量
        twenty=0 # 面额为20的数量
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            if bills[i]==10:
                if five==0:
                    return False
                ten+=1
                five-=1
            if bills[i]==20:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True

        
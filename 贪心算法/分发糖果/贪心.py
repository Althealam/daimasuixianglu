# 思路：
# 难点在于左右都需要兼顾，也就是ABC三个小孩，要判断A和B以及B和C多情况
# 两个小孩分数相同的情况下，则恢复糖果为1
# 1. 确定右小孩比左小孩得分高的情况:右小孩的candy比左小孩的candy多1个（从左往右遍历）
# if ratings[i+1]>ratings[i]: candy[i+1]=candy[i]+1
# 2. 确定左小孩比右小孩得分高的情况:左小孩的candy比右小孩的candy多1个（从右往左遍历）
# if ratings[i]>ratings[i+1]: candy[i]=candy[i+1]+1

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy=[1]*len(ratings)

        # 从前向后遍历，处理右侧比左侧评分高的情况
        for i in range(1,len(ratings)): # 需要从1开始遍历，因为下面会计算ratings[i-1]
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        
        # 从后向前遍历，处理左侧比右侧评分高的情况
        for i in range(len(ratings)-2,-1,-1): # 需要从len(ratings)-2开始遍历，因为下面会计算ratings[i+1]
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)
        
        result=sum(candy)
        return result
        

        
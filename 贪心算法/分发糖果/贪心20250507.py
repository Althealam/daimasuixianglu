# 思路：
# 1. 先从左边到右边，右孩子比左孩子大的情况：如果右边的孩子的评分比左边的孩子的评分高，则右边的孩子就比左边的孩子多一颗糖 candy[i]=candy[i-1]+1 
# 2. 再从右边到左边，左孩子比右孩子大的情况：如果左边的孩子的评分比右边的孩子评分高，则左边的孩子就比右边的孩子多一颗糖 candy[i]=max(candy[i], candy[i+1]+1)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy=[1]*len(ratings)
        # 先从左边到右边
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        # 再从右边到左边
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i], candy[i+1]+1)
        return sum(candy)


        
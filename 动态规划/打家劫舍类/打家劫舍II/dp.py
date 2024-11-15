# 本题与198打家劫舍的区别就是本题的房屋是成环状的
# 解决环的问题，以下只是考虑的范围，并不是一定要选择（1）考虑只要首元素，不要尾元素的范围，但是并不是一定要选首匀速（2）只要尾元素，不要首元素（3）首尾元素都不要
# 情况一和情况二包含了情况三，因此我们只需要求解情况二和情况三的最优解即可，并且情况二和情况三都是线性数组，不是环状的

# 时间复杂度：
# 1. 外层函数rob：
# （1）边界情况：O(1)
# （2）分别调用了两次robRange函数
# 2. robRange函数：
# （1）时间复杂度和nums_长度成线性关系，O(n)
# （2）每次调用robRange都会执行一个大小为n的动态规划过程
# 总的时间复杂度为O(n)

# 空间复杂度：
# 1. dp数组：dp数组长度为len(nums_)+1，因此空间复杂度为O(n)
# 2. rob和robRange还有常量空间的变量
# 总的空间复杂度为O(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        # 情况一：只考虑首元素，不考虑尾元素
        result1=self.robRange(nums,0,len(nums)-2)
        # 情况二：只考虑尾元素，不考虑首元素
        result2=self.robRange(nums,1,len(nums)-1)

        return max(result1,result2)
    
    # 打家劫舍的逻辑
    def robRange(self,nums,start,end):
        if start==end:
            return nums[start]

        nums_=nums[start:end+1]
        dp=[0]*(len(nums_)+1)
        dp[0]=nums_[0]

        if len(nums_)>=2:
            dp[1]=max(nums_[0],nums_[1])
            for i in range(2,len(nums_)):
                dp[i]=max(dp[i-2]+nums_[i],dp[i-1])
        return dp[len(nums_)-1]
        
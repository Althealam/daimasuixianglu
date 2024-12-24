# 分析：本题和全排列的区别在于给定一个可包含重复数字的序列，要返回所哟雨不重复的全排列
# 对于排列问题，树层上去重和树枝上去重都是可以的，但是树层上去重效率更高
# 1. 对树层中的前一位去重：used[i-1]==false
# 2. 对树枝前一位去重：used[i-1]==true
# 关于树层去重和树枝去重可以参考代码随想录里面该题的图
# 本题需要进行树枝和树层剪枝，并且不需要startIndex是因为这个顺序是可以打乱的
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        path=[]
        nums.sort() # 排序以方便去重
        used=[False]*len(nums)
        self.backstracking(nums,path,used,result)
        return result
    
    def backstracking(self,nums,path,used,result):
        # 收割结点的位置：当path的长度和nums相同的时候，到达叶子结点（终止条件）
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)): # 树层横向递归
            # 树层剪枝：not used[i-1]<->used[i-1]==False（树层剪枝需要保证两个元素是相等的）
            # 树枝剪枝：used[i]<->used[i]==True（取过的数直接跳过）
            # 关于树枝剪枝的更详细说明：比如[1,1,2]，第一个枝取1，该枝的分支可以出来[1,2]，但是为什么不是[1,1,2]呢
            # 这就是因为我们设置了used[0]=True，也就是说第一个1已经使用过了，因此这个枝我们需要剪去
            if (i>0 and nums[i]==nums[i-1] and used[i-1]==False) or used[i]==True:
                continue 
            # 这里必须是continue，不能是break，因为否则会误将其他的分支剪掉
            used[i]=True
            path.append(nums[i])
            # 树枝纵向递归
            self.backstracking(nums,path,used,result)
            # 回溯
            path.pop()
            used[i]=False # 回溯需要把used[i]设置为False，这也同样是为什么树层剪枝时为used[i-1]==False的原因

solution=Solution()
nums=[3,3,0,3]
result=solution.permuteUnique(nums)
print(result)
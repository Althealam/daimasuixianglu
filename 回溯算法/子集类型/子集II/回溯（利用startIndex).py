# 方法：回溯+利用递归的时候下一个startIndex是i+1而不是0去重
# 分析：本题就是子集+组合总和II的综合题目。这道题与上一道题的不同之处在于，这里有重复的元素，但是我们的子集不能出现重复，因此需要进行去重的操作
# 本题树层需要进行去重，但是树枝上不能进行去重，因为树枝上的重复代表的是不同元素，而树层上的重复代表的是相同的子集
# 子集的收获结果的位置都在结点处，并且子集一般不需要写终止条件，因为子集就是要遍历完整的树
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort() # 排序操作
        self.backstracking(nums,0,[],result)
        return result
    
    def backstracking(self,nums,startIndex,path,result):
        result.append(path[:]) # 收集子集
        for i in range(startIndex,len(nums)): # 树层操作
            if i>startIndex and nums[i]==nums[i-1]: # 树层剪枝操作
                continue
            path.append(nums[i])
            self.backstracking(nums,i+1,path,result) # 树枝操作
            path.pop() # 回溯操作


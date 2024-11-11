# 方法：回溯+利用used去重
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
        used=[False]*len(nums)
        nums.sort() # 排序操作
        self.backstracking(nums,0,used,[],result)
        return result
    
    def backstracking(self,nums,startIndex,used,path,result):
        # 进入递归后就是一个节点
        result.append(path[:]) # 收集子集
        # for循环相当于是树层操作
        for i in range(startIndex,len(nums)):
            # 数层去重（前提，需要对nums进行一个sort排序操作，让一样的元素放在一起）
            # 限制used[i-1]=False是因为要限制在树层去重，而不能在树枝上去重
            if i>0 and nums[i]==nums[i-1] and not used[i-1]: # 剪枝操作
                continue # 树层去重，之前取过一样的子集了，跳过这层循环
            # 对数组进行操作
            path.append(nums[i])
            used[i]=True
            # 递归操作（相当于是树枝操作）
            self.backstracking(nums,i+1,used,path,result)
            # 回溯操作
            used[i]=False
            path.pop()

        
# 分析：这道题目里有重复的元素，组合中的元素只能使用一次（组合的元素不可以重复，但是元素的数值是可以重复的），不能出现重复的组合
# 和之前的题目的区别：
# 1. 本题candidates中的每个数字在每个组合中只能使用一次
# 2. 本题数组candidates中的元素是有重复的，而之前的题目中的candidates是没有重复的
# 去重：以[1,1,5,6,2]为例
# 1. 树层去重：前面取过1了，后面的枝就不能再取1了
# 2. 树枝去重，需要有一个变量来告诉我们哪些字段使用过了
# 递归三部曲：
# 1. 递归函数参数：需要增加一个used来记录同一树枝上的元素是否使用过；result存放组合集合；path存放符合条件的数组
# 2. 递归终止条件：sum>target 和 sum==target
# 3. 单层搜索的逻辑：需要进行去重

class Solution(object):
    def backstracking(self,candidates,target,sum,startIndex,used,path,result):
        if sum==target:
            result.append(path[:])
            return
        for i in range(startIndex,len(candidates)):
            # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
            if i>startIndex and candidates[i]==candidates[i-1] and not used[i-1]:
                continue
            if sum+candidates[i]>target:
                break
            
            sum+=candidates[i]
            path.append(candidates[i])
            used[i]=True
            self.backstracking(candidates,target,sum,i+1,used,path,result)
            used[i]=False
            sum-=candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        used=[False]*len(candidates)
        result=[]
        candidates.sort() # 排序，让相同的元素放在一起
        self.backstracking(candidates,target,0,0,used,[],result)
        return result
        
# 回溯法
class Solution(object):
    def backstracking(self,candidates,target,total,startIndex,path,result):
        if total==target:
            result.append(path[:])
        # 如果sum+candidates[i]>target，则停止遍历
        for i in range(startIndex,len(candidates)):
            if total+candidates[i]>target:
                break
            total+=candidates[i]
            path.append(candidates[i])
            self.backstracking(candidates,target,total,i+1,path,result)
            total-=candidates[i]
            path.pop()

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total=sum(nums)
        if target>total:
            return 0
        if (target+total)%2!=0:
            return 0
        bagSize=(target+total)//2 # 转化为组合总和问题，bagsize就是目标和

        # 回溯法代码
        result=[]
        nums.sort()
        self.backstracking(nums,bagSize,0,0,[],result)
        return len(result)
        
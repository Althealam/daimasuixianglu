# 分析：组合问题和分割问题都是收集树的叶子结点，而子集问题是找树的所有节点
# 子集也是一种组合问题，因为它的集合是无序的，在无序的情况下，取过的元素不会重复取，因此写回溯算法时，for要从startIndex开始，而不是从0开始
# 1. 递归函数的参数：path为子集收集元素，二维数组result存放子集组合，并且还需要startIndex
# 2. 递归终止条件：剩余集合为空的时候就是叶子结点，也就是startIndex>len(nums)的时候终止了，因为没有元素可以取
# 3. 单层搜索逻辑：求取子集问题，不需要剪枝

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backstracking(nums,0,[],result)
        return result

    def backstracking(self,nums,startIndex,path,result):
        result.append(path[:]) # 收集子集，要放在终止条件的上面
        # 终止条件
        if startIndex>=len(nums):
            return
        for i in range(startIndex,len(nums)):
            path.append(nums[i]) # 处理结点
            self.backstracking(nums,i+1,path,result) # 递归
            path.pop() # 回溯

        
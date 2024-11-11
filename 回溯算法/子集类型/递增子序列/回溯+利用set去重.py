# 方法：回溯+利用set去重
# 分析：递归三部曲
# 1. 递归函数参数：二维数组result，一维数组path，startIndex来调整下一层递归的起始位置（一个元素不能重复使用）
# 2. 终止条件：可以不加终止条件，因为子集问题是要遍历树形结构找每一个节点
# 3. 单层搜索逻辑：同一父节点下的同层上使用过的元素就不能再使用了
# 树层递归：在当前层次上遍历不同的选项，相当于水平扩展每个递归路径
# 树枝递归：沿着每一个选型进一步递归，相当于从当前选项向下深入
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        path=[]
        self.backstracking(nums,0,path,result)
        return result
    
    def backstracking(self,nums,startIndex,path,result):
        # 对节点进行判断，只要节点(path)的数量大于1，就收获结点
        if len(path)>1:
            result.append(path[:]) # 使用切片将当前路径加入结果集
        
        # 取数逻辑
        uset=set() # 使用集合对本层元素进行去重（记录本层中取到的元素）
        for i in range(startIndex,len(nums)): # 树层
            # 去重
            # 如果path不为空，并且nums[i]比path最右边的元素小，或者nums[i]在uset中，则不考虑这个分支
            if (path and nums[i]<path[-1]) or nums[i] in uset:
                # path[-1]为path里面最右边的元素
                continue # 应该使用continue而不是break，因为可能这个父结点还可以有其他的分支
            
            # 取元素
            uset.add(nums[i]) # 记录这个元素在本层中使用过了
            path.append(nums[i]) # 将nums[i]添加到path中
            self.backstracking(nums,i+1,path,result) # 纵向扩展（树枝）
            path.pop() # 回溯
        
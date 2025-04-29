# 时间复杂度：O(n*2**n)
# 1. 排序：O(nlogn)
# 2. 回溯：对于一个长度为n的数组， 子集的数量为2**n。对于每个子集，都要复制子集放到结果集中，path[:]的时间复杂度为O(k)
# 因此回溯的时间复杂度为O(n*2**n)

# 空间复杂度：O(n*2**n)
# 1. 递归调用栈的深度：数组的长度为n，数的最大深度为n
# 2. 存储结果需要的空间：每个数组最大长度为n，最多要存储2**n个数组
# 3. 存储临时子集：path为n

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        nums.sort()
        self.traversal(result, path, nums, 0)
        return result

    def traversal(self, result, path, nums, startIndex):
        if path not in result:
            result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(result, path, nums, i+1)
            path.pop()        
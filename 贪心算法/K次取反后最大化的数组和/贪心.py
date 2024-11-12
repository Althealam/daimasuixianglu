# 思路：
# 1. 正数和负数中，优先对负数进行取反
# 2. 负数中，优先对绝对值最大的负数取反（通过对nums进行排序来实现）
# 3. 上述两步过后，如果k还没用完，则对正数中最小的数进行取反

# 时间复杂度：
# 1. 排序操作：sort排序的时间复杂度为O(nlogn)
# 2. 遍历数组：for i in range(len(nums))的时间复杂度为O(n)
# 3. 对数组的剩余操作：O(1)
# 4. 求和操作：O(n)
# 总的时间复杂度为O(nlogn)

# 空间复杂度：
# 1. nums排序后输入数组nums：O(n)
# 2. 额外的变量k、i、result：O(1)
# 总的空间复杂度为O(n)
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 第一步：按照绝对值降序排序数组nums
        nums.sort(key=lambda x: abs(x),reverse=True) 

        # 第二步：执行K次取反操作（因为前面已经排序了，因此可以保证是对绝对值最大的负数进行取反）
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]*=-1 # 取反
                k-=1 # 减去一个次数
        
        # 第三步：如果k还有剩余次数，将绝对值最小的元素取反
        # k%2==0也就是说k为偶数，那么我们就把所有的负数都取反偶数次，可以得到同样的非负值
        # k%2==1也就是说k为奇数，那么我们就把最小的正数取反，可以让我们的损失最小
        if k%2==1:
            nums[-1]*=-1

        # 第四步：计算数组nums的元素和
        result=sum(nums)
        return result
        
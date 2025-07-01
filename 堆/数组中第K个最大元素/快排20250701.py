# 思路：使用快排，将大于基准的元素放到右子数组，将小于基准的元素放到左子数组
# 然后判断左右子数组的大小来判断第K大的元素在左右子数组中的哪一个

# 时间复杂度：O(n)
# （1）对于长度为n的数组执行划分的时间复杂度为O(n)
# （2）每轮哨兵划分后，向下递归子数组的平均长度为n/2
# （3）平均情况下，哨兵划分操作一共有n+n/2+n/4+...=2n-1，复杂度为O(n)
# 空间复杂度：O(logn)，划分函数的平均递归深度为logn
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_selection(nums, k):
            # 划分数组
            pivot = nums[-1]
            big, equal, small = [], [], []
            for num in nums:
                if num>pivot:
                    big.append(num)
                elif num<pivot:
                    small.append(num)
                else:
                    equal.append(num)
            
            # 判断k和数组的大小
            if k<=len(big): # 第k大的元素在big中
                return quick_selection(big, k)
            if len(nums)-len(small)<k: # 第k大的元素在small中
                return quick_selection(small, k-len(nums)+len(small))
            return pivot
        return quick_selection(nums, k)
        
            
    
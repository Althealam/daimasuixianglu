# 方法：利用map哈希求解
# 重点：遇到判读这个元素是否出现过/这个元素是否在这个集合里出现过-->使用哈希法
# 思路：需要知道这个元素是否出现过（map的key）并且还要知道这个元素在数组里的下标（map的value）-->使用map

# 数组和set来做哈希法的局限：
# 1. 数组的大小是受到限制的，而且如果元素很少，而且哈希值太大会造成内存空间的浪费；
# 2. set是一个集合，里面放的元素只能是一个key，而两数之和这道题目不仅要判断y是否存在，还要记录y的下标位置，因为要返回x和y的下标，所以set也不能用。

# 解题过程：
# map的作用：用来存放遍历过的元素，因为遍历数组的时候，需要记录我们之前遍历过哪些元素和对应的下标，这样才能找到与当前元素相互匹配的
# map的存储结构：{key:数据元素, value: 数组元素对应的下标}
# 在遍历数组的时候，需要向map查询是否有和目前遍历元素匹配的数值，如果有，就找到了匹配对象，如果没有，就把目前遍历的元素放到map中。

# 时间复杂度：O(n)
# 空间复杂度：O(n)，其中n是nums的长度，因为可能需要将列表中的所有元素以及其索引存放早字段records中（字段的空间占用与存储的键值对数量成正比）

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建一个集合来存储我们目前看到的数字
        seen=set()
        # 第一个方法是使用字段来存储
        for i,num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [nums.index(complement),i]
                # nums.index(complement)：找到补数在列表中首次出现的索引
            seen.add(num)
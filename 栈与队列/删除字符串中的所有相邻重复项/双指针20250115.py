# 思路：双指针法
# 将不重复的元素依次移动到列表的前面，用slow的前进和后退来处理相邻元素
# 定义slow和fast，用slow来存储所有的不重复元素，用fast来遍历所有的字符（遍历条件是fast<len(result)）
# 每次遍历字符串的时候，都用fast来覆盖slow
# 如果slow和slow-1相等，则将slow回退一个，并且同样的用fast覆盖

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # slow指向不重复的元素
        slow=0
        # fast遍历字符串中所有的元素
        fast=0
        # 将字符串变成数组的形式
        result=list(s)
        # 开始遍历字符串
        while fast<len(result):
            # 用fast来覆盖slow
            result[slow]=result[fast]
            # 1. slow和fast指向的元素相同：直接覆盖
            # 2. slow和fast指向的元素不同：fast遍历的元素进行覆盖

            # 如果发现slow指向元素和前一个一样，则退一个指针
            if result[slow]==result[slow-1] and slow>0:
                slow-=1
            # 如果发现slow指向元素和前一个不同，则进一个指针
            else:
                slow+=1
            # 继续移动fast指针
            fast+=1
        return ''.join(result[0:slow])
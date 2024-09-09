# 方法一：使用栈
# 思路：用一个栈保存遍历过的元素
# 遍历元素时，比较栈里有没有出现遍历的元素，如果有的话就弹出栈内相同的元素
# 如果又遇到相同的元素，可以继续从栈中弹出该元素
# 分析：我们可以用字符串模拟栈
# 时间复杂度：O(n) 遍历字符串s中的每个字符
# 空间复杂度：O(n) res列表用于存储去重后的字符，其最大大小不会超过原始字符串s的长度，在最坏情况下，字符串没有重复字符

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list()
        # 也可以写成res=[]
        for item in s:
            if res and res[-1]==item:
                res.pop()
            else:
                res.append(item)
        return "".join(res) # 字符串拼接
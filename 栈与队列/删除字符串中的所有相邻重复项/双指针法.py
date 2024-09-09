# 方法二：双指针法
# 思路：使用双指针模拟栈
# 空间复杂度：O(1) 不需要额外的空间来存储结果，而是直接在原字符串上进行操作
# 时间复杂度：O(n)，因为fast指针会遍历整个字符串一次
# 分析：fast指针遍历字符串的每个字符；slow指针用于跟踪结构字符串的当前长度
# 当fast指针指向的字符与slow指针前一个字符（结果字符串的最后一个字符）相同时，slow指针回退一位，表示要移除这个重复的字符
# 当fast指针指向的字符与slow指针前一个字符不同时，将fast指针指向的字符复制到slow指针的位置，并将slow指针前进一步，表示在结果字符串中添加了一个新的字符
# slow并不是在字符串上移动，而是在结果数组中移动，它表示结果数组的当前有效长度

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list(s)
        slow=fast=0
        length=len(res)

        while fast<length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow]=res[fast]

            # 如果发现和前一个一样，就退一格指针
            # 如果slow指针不是在列表的开始位置(slow>0)，并且slow指针指向的字符与它前一个字符相同
            # 那么slow指针向前移动一位（跳过重复的字符，不将它们包含在最终的结果中）
            if slow>0 and res[slow]==res[slow-1]:
                slow-=1
            else:
                # 如果slow指针指向的字符与它前一个字符不相同，那么slow指针就向前移动一位
                # 表示我们已经找到了一个不重复的字符
                slow+=1
            fast+=1

        return ''.join(res[0:slow]) # 获取结果数组中从0到slow的所有元素（这些元素组成了没有相邻重复字符的结果字符串）
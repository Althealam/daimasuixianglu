# 方法二：使用字典
# 思路：如果遇到左括号，就让右括号进栈；遇到左花括号，就要右花括号进栈
# 最后开始遍历栈，如果遇到右边的括号就弹出
# 如果字符串的长度为奇数，那么一定有不匹配的，直接返回false
# 分析：
# 1. 第一种情况：字符串里左方向的括号多余了，所以不匹配
# 2. 第二种情况：括号没有多余，但是括号的类型没有匹配上
# 3. 第三种情况：字符串里右方向的括号多余了，所以不匹配
# 结果：
# 1. 第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配
# 2. 第二种情况：遍历字符串匹配的过程中，发现栈里没有要匹配的字符
# 3. 第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号
# 左右括号匹配的情况：字符串遍历完后，栈是空的

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping={
            '(':')',
            '[':']',
            '{':'}'
        }
        # key: (, [, {
        # value: ), ], }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
                # 和第一种方法不同的是，用mapping的方法来入栈元素
            elif not stack or stack[-1]!=item:
                # 判断stack是否为空或者栈顶元素不一致
                return False
            else:
                stack.pop()
        return True if not stack else False
                

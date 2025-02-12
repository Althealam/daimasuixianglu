# 思路：
# 1. 递归函数的参数和返回值：
# path路径，result结果集，startIndex下一层搜索的起始位置, digits字符串
# 2. 递归的终止条件：
# len(path)==len(digits): result.append(''.join(path)) return
# 3. 单层搜索的逻辑：
# （1）获取当前搜索的位置对应的索引：index=int(digits[startIndex])
# （2）获取该索引对应的映射：letters=lettermap[index]
# （3）遍历该索引下的字母来获取path并回溯：
# path.append(letter) self.backtracking(...) path.pop()

# 时间复杂度：O(4^n*n)
# 假设输入字符串digits的长度为2，那么如果按下2和3，那么可能的结果数为3x3
# 假设输入字符串digits的长度为n，那么可能的结果数最多为4^n（因为9和7都是4个数字）
# 对于每个生成的组合都要用''.join(path)，该操作的时间复杂度为O(n)

# 空间复杂度：O(4^n*n)
# 1. 递归调用栈的空间：递归的深度最大为n
# 2. 存储结果的空间，最坏情况下组合数为4^n，每个组合的长度为n


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 映射关系，0映射"", 1映射"", 2映射"abc"
        self.lettermap=[
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        result=[] # 结果集
        # 特殊情况判断
        if len(digits)==0:
            return []
        self.backtracking([],result,0, digits)
        return result

    
    def backtracking(self, path, result, startIndex, digits):
        # 终止条件
        if len(path)==len(digits):
            result.append(''.join(path))
            return
        # 获取数字
        digit=int(digits[startIndex])
        # 获取该数字对应的映射
        letters=self.lettermap[digit]
        # 遍历映射
        for letter in letters:
            path.append(letter)
            self.backtracking(path, result, startIndex+1, digits)
            path.pop()
            


        
        


        
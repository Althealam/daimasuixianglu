# 方法：回溯法
# 分析：输入的数字的个数，决定了我们的树的深度；树的宽度有输入的数字的长度来决定

# 时间复杂度：
# 1. 回溯树的结果：如果输入字符串digits的长度为n，那么回溯树的深度为n
# 在每一层，我们有最多4个分支，即每个数字最多可以生成4种组合，因此回溯树的最大节点树为4^n
# 2. 每次操作的代价：
# （1）递归调用的操作代价为O(1)（字符拼接、索引操作、添加结果）
# （2）结果中每个组合的长度为n，最终有4^n个组合
# 总的时间复杂度为O(4^n)
# 空间复杂度：
# 1. 递归栈的深度：递归栈的最大深度为 n，所以递归栈的空间复杂度是 O(n)。
# 2. 存储结果：self.result存储了所有的组合，最多有4^n个组合，每个组合的长度为n
# 3. 存储当前路径的空间：每次递归调用只保留当前路径 self.s，其空间复杂度为 O(n)。
# 总的空间复杂度：O(n*4^n)

class Solution(object):
    def __init__(self):
        # 做映射
        # letterMap[2]="abc"
        # letterMap[3]="def"
        self.letterMap=[
            "", # 0
            "", # 1
            "abc", # 2
            "def", # 3
            "ghi", # 4
            "jkl", # 5
            "mno", # 6
            "pqrs", # 7
            "tuv", # 8
            "wxyz" # 9
        ]
        self.result=[]
        self.s=""

    def backstracking(self,digits,index):
    # index用来遍历给出的字符串已经遍历到哪个位置了
    # 这里不需要使用startindex是因为，现在取数的是两个集合，不用避免重复
        if index==len(digits):
            self.result.append(self.s)
            return
        digit=int(digits[index]) # 将索引处的数字转换为整数
        letters=self.letterMap[digit] # 获取对应的字母集合
        for i in range(len(letters)):
            self.s+=letters[i] # 处理字符
            self.backstracking(digits,index+1) # 递归调用，注意索引+1，处理下一个数字
            # 切片操作，s[:-1]会返回从第一个元素到倒数第二个元素的子序列，相当于“从头开始，去掉最后一个元素”
            self.s=self.s[:-1] # 回溯，删除最后添加的字符

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return self.result
        self.backstracking(digits,0)
        return self.result
        
# 分析：可以根据对该数字进行分割来绘制树形图
# 1. 定义递归函数的参数和返回值：startIndex（不能重复分割）记录下一层递归分割的起始位置，pointNum记录添加逗点的数量
# 2. 递归终止条件：题目要求只会分成4段，因此pointSum=3的时候，就说明字符串分成4段了，然后验证一下第四段是否合法，合法的话就加入到结果集里
# 3. 单层搜索的逻辑：截取的子串[startIndex,i]，判断该子串是否合法，合法的话就在字符串后面加上符号.，表示已经分割
# 如果不合法就结束本层循环
# 递归：递归调用时，下一层递归的startIndex要从i+2开始（因为在字符串中加入了分隔符.），同时记录分割符的数量pointNum要+1
# 回溯：将刚刚加入的分割符删除，并且pointNum-1

# 时间复杂度：
# 1. 回溯过程
# 2. 判断子串是否合法：每一层递归中，is_valid函数都被调用来验证一个子串是否是有效的IP地址段，时间复杂度为O(k)，其中k是子串的长度
# 3. 递归的深度：需要将字符串分割成4段，因此递归的深度为4
# 4. 回溯的分支树：对于一个长度为n的字符串，最大分支树为n^3（需要遍历字符串并且每次尝试从当前起始点切割一个子串，这个分支数在最坏情况下是三次选择）
# 每次切割1-3个字符，乘以递归深度（3个点）
# 总体时间复杂度：O(n^3)

# 空间复杂度：
# 1. 递归栈的空间：递归的深度为4
# 2. 存储路径的空间：假设有k个有效的地址，并且每个地址的长度为n，因此存储这些地址需要的空间为O(k*n)
# 3. 总空间复杂度：O(k*n)

# 回溯过程的核心步骤：
# 1. 递归树的形成：
# （1）每次递归都会在字符串的不同位置进行切割，即通过移动startIndex来逐步切割字符串。每个切割位置都会产生一个新的子字符串
# （2）在每次递归的过程中，pointNum表示已切割的段数，最后一段由startIndex和字符串的结尾决定
# 2. 合法性检查
# （1）对于每一段子字符串，都会使用 is_valid 方法进行检查，确保每一段 IP 地址是合法的。
# （2）合法的条件是：如果子字符串以 0 开头，必须只包含一个字符（即 0 本身）；子字符串必须是数字，且值不能超过 255。
# 3. 递归中的分割探索：
# （1）每次递归调用都会在当前分割点继续切割。比如，在第一轮递归中，尝试将字符串的每个可能的子字符串作为第一个 IP 地址段（即 sub = s[startIndex:i+1]）。
# （2）如果该子字符串是有效的（通过 is_valid 判断），则递归调用继续从新的起始点进行切割。
# （3）如果某个分割点的子字符串不合法（即 is_valid 返回 False），则跳过当前的循环，继续尝试下一个可能的分割点。
# 4. 回溯的核心
# （1）递归中的回溯体现在 current 字符串和 pointNum 计数器的更新与回退上：
#       current用来存储当前的IP地址部分
#       当递归走到分割的末尾时（即 pointNum == 3），检查剩余的部分是否合法。如果合法，将其加入到 current 中并保存。
#       在递归返回时，会通过 current + sub + '.' 将当前的 IP 地址段连接到结果列表中，完成一个有效的分割过程。
#       如果某次分割不成功，current 会被回溯（即 current 被重置），以便继续尝试不同的分割方式。
# 5. 递归终止条件
# （1）当 pointNum == 3 时，意味着已经切割了 3 个有效的段，此时检查剩余的部分是否也能作为一个合法的 IP 地址段。
# （2）如果剩余部分合法，就将其加入 current，并将 current 完整的 IP 地址保存到结果列表 result 中。

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        self.backtracking(s,0,0,"",result)
        return result
    
    def backtracking(self,s,startIndex,pointNum,current,result):
        # 递归终止的条件
        if pointNum==3: # 逗点数量为3，分割结束（判断最后一个子字符串是否合法）
            if self.is_valid(s,startIndex,len(s)-1): # 判断第四段子字符串是否合法（左闭右闭区间）
                current+=s[startIndex:] # 添加最后一段字符串到current里面
                result.append(current) # 最后一段合法后，收集结果
            return
        # 单层搜索的逻辑（相当于一个个切割的过程）
        for i in range(startIndex,len(s)):
            if self.is_valid(s,startIndex,i): # 判断[startIndex,i]这个区间的子串是否合法
                sub=s[startIndex:i+1] # 子字符串
                self.backtracking(s,i+1,pointNum+1,current+sub+'.',result)
            else: # 如果不合法的话，直接跳出这个循环
                break
    
    def is_valid(self,s,start,end):
        if start>end:
            return False
        if s[start]=='0' and start!=end:
            return False
        num=0
        for i in range(start,end+1):
            if not s[i].isdigit(): # 遇到的非数字字符不合法
                return False
            num=num*10+int(s[i])
            if num>255:
                return False
        return True


    
        
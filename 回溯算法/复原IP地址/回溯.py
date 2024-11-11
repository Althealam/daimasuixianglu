
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

solution=Solution()
input_string='25525511135'
result = solution.restoreIpAddresses(input_string)
    
        
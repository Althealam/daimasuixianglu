# 思路：利用i遍历数组s，并且每次以2k为一段来进行反转
# for(i=0;i<s.size;i+=2k)
#   if i+k<=s.size():
#       reverse(s,i,i+k);
#       continue;
#   reverse(s,i,s.size);
# 1. 使用range(start,end,step)来确定需要调换的初始位置；
# 2. 对于字符串s='abc' 如果使用s[0:999]===>'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理；
# 3. 用切片整体替换，而不是一个个替换
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# res是一个列表，用与存储字符串s的字符。这个列表的长度和字符串s的长度相同，即O(n)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse_substring(text): # 定义一个函数，用来交换位置
            left,right=0,len(text)-1
            while left<right:
                text[left],text[right]=text[right],text[left] 
                left+=1
                right-=1
            return text

        res=list(s)

        for cur in range(0,len(s),2*k):
            res[cur:cur+k]=reverse_substring(res[cur:cur+k])
        
        return ''.join(res)
        # 将列表中的字符串元素连接起来并返回一个新的字符串
        # res是一个列表，并且列表中的每个元素都是字符串
        # join()方法遍历列表res中的每个元素
        # 它将这些元素按照它们在列表中的顺序连接起来，元素之间不添加任何分隔符
        # Eg：res=['He','llo','World']
        # 返回：'Hello World'
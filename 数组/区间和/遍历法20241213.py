# 时间复杂度：O(n)
# 空间复杂度：O(n)
# 思路：
# 1. 计算每个index的累加区间和
# 2. 计算对应interval的区间和
# （1）interval_start==0：该interval的区间和为interal_end对应的区间和
# （2）interval_start!=0: 该interval的区间和为interval_end的累计区间和-interval_start-1的区间和


import sys
# 从标准输入读取数据
input=sys.stdin.read()

def main():
    input_data=input.split()
    # n是数组的元素个数
    n=int(input_data[0])
    
    # vector是数组元素
    vector=[]
    for i in range(1,n+1):
        vector.append(int(input_data[i]))
    
    # interval_sum是数组中每个元素的累积和
    interval_sum=[0]*n
    pre_sum=0
    for i in range(n):
        pre_sum+=vector[i]
        interval_sum[i]=pre_sum

    # interval是区间值  
    interval=[]
    for i in range(1+n,len(input_data)):
        interval.append(input_data[i])
    
    # result是利用区间值得到的区间和，也就是最终的返回值
    result=[]
    index=0
    while index<len(interval):
        interval_start=int(interval[index])
        interval_end=int(interval[index+1])
        
        if interval_start==0:
            result.append(interval_sum[interval_end])
        else:
            result.append(interval_sum[interval_end]-interval_sum[interval_start-1])
        index+=2
    
    for r in result:
        print(r)

if __name__=='__main__':
    main()
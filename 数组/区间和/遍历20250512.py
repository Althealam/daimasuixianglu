import sys
input=sys.stdin.read()
input_data=input.split()
# 元素的个数
n=int(input_data[0])
nums=[]
for i in range(1, n+1):
    nums.append(int(input_data[i]))
# 计算intervals的值
intervals=[0]*len(nums)
pre_sum=0
for i in range(len(intervals)):
    pre_sum+=nums[i]
    intervals[i]=pre_sum
# print(intervals)


result=[] # 区间和返回值

# 读取区间的下标
index=1+len(intervals)
while index<len(input_data):
    intervals_start=int(input_data[index])
    intervals_end=int(input_data[index+1])
    if intervals_start==0:
        result.append(intervals[intervals_end])
    else:
        result.append(intervals[intervals_end]-intervals[intervals_start-1])
    index+=2

for r in result:
    print(r)


import sys
input = sys.stdin.read()
input_data = input.split()
n = int(input_data[0])
nums = []
for i in range(1, n+1):
    nums.append(int(input_data[i]))

intervals = [0]*len(nums)
intervals[0] = nums[0]
for i in range(1, len(intervals)):
    intervals[i] = intervals[i-1]+nums[i]

index = 1+len(nums)
while index<len(input_data):
    interval_start = int(input_data[index])
    interval_end = int(input_data[index+1])
    if interval_start==0:
        print(intervals[interval_end])
    else:
        print(intervals[interval_end]-intervals[interval_start-1])
    index+=2
    

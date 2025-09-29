# 会议室安排
# 已知有多个会议的开始时间和结束时间，至少需要多少个会议室才能并行的召开
# 会议：[(1, 3), (3, 5), (2, 4)]
# 会议室个数：2个

def min_arrangement(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1)) # 会议开始
        events.append((end, -1)) # 会议结束
    
    # 排序：时间小的排在前面，同一时刻结束要排在开始之前
    events.sort(key = lambda x: (x[0], x[1]))

    rooms, res = 0, 0
    for _, e in events:
        rooms+=e
        res = max(res, rooms)
    return res

intervals = [[1, 3], [3, 5], [2, 4]]
print(min_arrangement(intervals))
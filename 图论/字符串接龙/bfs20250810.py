n = int(input())
beginStr, endStr = map(str, input().split())
str_list = []
for _ in range(n):
    str_list.append(str(input()))

if beginStr == endStr:
    print(0)
    exit()

def judge(s1, s2):
    """判断s1到s2之间是否有一条路径"""
    count = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1 # 如果只是有一个字符不一样，那么有一条路径

from collections import deque
step = 1
visited = [False for i in range(n)]
queue = deque()
queue.append([beginStr, step])
while queue:
    str_new, step = queue.popleft()
    if judge(str_new, endStr):
        print(step+1)
        exit()
    for i in range(n):
        if not visited[i] and judge(str_list[i], str_new):
            visited[i] = True
            queue.append([str_list[i], step+1])

print(step)

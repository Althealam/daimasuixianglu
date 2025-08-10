from collections import deque
n = int(input())
beginStr, endStr = map(str, input().split())
str_list = []
for _ in range(n):
    str_list.append(str(input()))

if beginStr==endStr:
    print(0)
    exit()

def judge(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    return count==1

visited = [False]*n
queue = deque()
step = 1
queue.append([beginStr, step])
found = False
while queue:
    current_str, step = queue.popleft()
    if judge(current_str, endStr):
        found = True
        print(step+1)
        exit()
    for i in range(len(str_list)):
        if not visited[i] and judge(str_list[i], current_str):
            visited[i] = True
            queue.append([str_list[i], step+1])

if not found:
    print(0)
    exit()

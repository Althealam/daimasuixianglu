import collections

n = int(input())
beginStr, endStr = map(str, input().split())
str_list = []
for _ in range(n):
    str_list.append(str(input()))

def judge(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            cnt+=1
    return cnt==1

def find_path(beginStr, endStr, str_list):
    if beginStr==endStr:
        print(0)
        exit()
    visited = [False]*len(str_list)
    queue = collections.deque()
    step = 1
    queue.append([beginStr, step])
    while queue:
        current_str, current_step = queue.popleft()
        if judge(current_str, endStr):
            print(current_step+1)
            exit()
        for i in range(len(str_list)):
            if not visited[i] and judge(current_str, str_list[i]):
                visited[i] = True
                queue.append([str_list[i], current_step+1])
    print(0)
    exit()

find_path(beginStr, endStr, str_list)

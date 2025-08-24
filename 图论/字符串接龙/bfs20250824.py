from collections import deque 
n = int(input()) # strList中的字符串数量
beginStr, endStr = map(str, input().split())
str_list = []
for _ in range(n):
    str_list.append(str(input()))

if beginStr == endStr:
    print(0)
    exit()

def judge(str1, str2):
    """判断str1和str2之间是否有路径"""
    cnt = 0 # str1和str2不同的字符个数
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            cnt+=1
    return cnt==1 # 如果cnt为1那么就有路径，否则没有路径

def find_path(beginStr, endStr, str_list):
    visited = [False]*len(str_list)
    queue = deque()
    step = 1 # 记录需要的字符串数量
    queue.append([beginStr, step])
    found = False
    while queue:
        current_str, current_step = queue.popleft()
        if judge(current_str, endStr):
            print(current_step+1)
            found = True
            exit()
        for i in range(len(str_list)):
            if not visited[i] and judge(current_str, str_list[i]):
                visited[i] = True
                queue.append([str_list[i], current_step+1])
    if not found:
        print(0)
        exit()

find_path(beginStr, endStr, str_list)
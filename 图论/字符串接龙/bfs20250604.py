# 思路：
# 1. 构建图，求出图中的最短路径的长度
# 2. 图中的线：通过枚举，用26个字母替换当前字符中的每一个字符，查看替换后的字符是否在strList中出现过，就可以判断两个字符串是否是连接的
# 3. 点与点之间的关系：判断是否差一个字符，如果差一个字符，就是有连接

# 无权图中，用bfs最合适，因为bfs只要搜到了终点就是最短路径

# ==========读取数据=============
# 读取字典的字符串数量
n=int(input())
# 读取起始字符和结束字符
beginstr, endstr = map(str, input().split())
if beginstr==endstr:
    print(0)
    exit()
# 读取strList中的字符串
strlist=[]
for i in range(n):
    strlist.append(input())

# =======判断两个字符串中的连接=========
def judge(s1, s2):
    """
    判断s1到s2之间是否有连接
    如果两个字符串之间相差一个字符，那么就是有连接
    """
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1

# ========BFS求最小步数========
# 使用bfs
visited=[False for i in range(n)]
queue=[[beginstr, 1]] # 加入当前遍历的字符串和步数
while queue:
    cur_str, step=queue.pop() 
    # 目前遍历的cur_str到endstr有线
    if judge(cur_str, endstr):
        print(step+1)
        exit()
    for i in range(n):
        if not visited[i] and judge(strlist[i], cur_str):
            visited[i]=True
            queue.append([strlist[i], step+1])
print(0)
# 思路：有向图搜索全路径
# DFS三部曲：
# 1. 确定递归函数，参数
# 2. 确定终止条件
# 3. 处理目前搜索节点出发的路径

import collections 
path=set()
def bfs(graph, i):
    global path # 记录从节点1出发时经过的所有节点
    que=collections.deque([i])
    while que:
        cur=que.popleft()
        path.add(cur)
        for nei in graph[cur]:
            que.append(nei)
        graph[cur]=[] # 清空cur的连接节点值
    return 



def main():
    # n为节点数量，k为边的数量
    n, k = map(int, input().split())
    # 构建有向图矩阵，表示每个节点的连接节点
    graph=[[] for _ in range(n+1)]
    for _ in range(k):
        s, t = map(int, input().split())
        graph[s].append(t)

    # 从节点1开始搜索
    bfs(graph, 1)

    # 判断path是否包含了所有的节点值
    if path=={i for i in range(1, n+1)}:
        return 1
    return -1

if __name__=='__main__':
    print(main())

# BFS

import collections

path=set() # 记录BFS所经过的节点

def bfs(root,graph):
    """
    从起点节点root开始执行广度优先搜索
    """
    global path

    # 双端队列que，将起始节点入队
    # BFS的核心思想是通过队列逐层访问图中的节点
    que=collections.deque([root])
    # 开始BFS遍历，只要队列中有节点未被处理，循环就继续
    while que:
        cur=que.popleft() # 从队列的左端取出一个节点cur，这是正在处理的节点
        path.add(cur) # 将当前节点cur添加到path中
        
        for nei in graph[cur]: # 遍历当前节点cur的所有邻居节点
            que.append(nei) # 将邻居节点nei入队，表示下一步需要访问的节点
        
        graph[cur]=[] # 将当前节点的邻居列表清空
    return

def main():
    N,K=map(int,input().strip().split()) # 图中节点数、图中边数
    graph=collections.defaultdict(list) # 图的邻接表
    # 循环读取K条边的信息
    for _ in range(K):
        # 从输入中读取一条边的起点src和终点dest
        src,dest=map(int,input().strip().split())
        # 在邻接表中记录这条有向边
        graph[src].append(dest)

    # 从节点1开始执行BFS比哪里    
    bfs(1,graph)
    # 判断BFS遍历经过的节点集合path是否等于从1到N的所有节点集合
    if path=={i for i in range(1,N+1)}:
        return 1
    return -1

if __name__=='__main__':
    print(main())
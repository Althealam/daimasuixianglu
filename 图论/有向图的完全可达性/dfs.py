# 有向图搜索全路径
# DFS三部曲
# 1. 确定递归函数，参数：需要传入地图，最坏掉我们当前拿到的key；同时还需要一个数组，用来记录我们都走过了哪些房间
# 2. 确认终止条件：如果是处理当前访问的节点，当前访问的节点为True，表示已经访问过了，则终止递归；否则，将其赋值为True
# 3. 处理目前搜索节点出发的路径

def dfs(graph,key,visited):
    for neighbor in graph[key]:
        if not visited[neighbor]:
            visited[neighbor]=True
            dfs(graph,neighbor,visited)

def main():
    import sys
    input=sys.stdin.read
    data=input().split()
    
    n=int(data[0]) # 节点数
    m=int(data[1]) # 边数
    
    graph=[[] for _ in range(n+1)]
    index=2
    for _ in range(m):
        s=int(data[index])
        t=int(data[index+1])
        graph[s].append(t)
        index+=2
    
    visited=[False]*(n+1)
    visited[1]=True
    dfs(graph,1,visited)
    
    for i in range(1,n+1):
        if not visited[i]:
            print(-1)
            return
        
    print(1)

if __name__=='__main__':
    main()
    
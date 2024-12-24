# 有向图搜索全路径
# DFS三部曲
# 1. 确定递归函数，参数：需要传入地图，最坏掉我们当前拿到的key；同时还需要一个数组，用来记录我们都走过了哪些房间
# 2. 确认终止条件：如果是处理当前访问的节点，当前访问的节点为True，表示已经访问过了，则终止递归；否则，将其赋值为True
# 3. 处理目前搜索节点出发的路径

def dfs(graph,key,visited):
    """
    遍历图的所有路径
    :param graph: 图的邻接表表示（一个二维列表）
    :param key: 当前节点的编号（我们正在访问的节点）
    :param visited: 一个布尔列表，记录每个节点是否已经访问过
    """

    # 遍历当前节点key的所有邻居节点（即直接与key有边相连的节点）
    for neighbor in graph[key]:
        if not visited[neighbor]: # 检查邻居节点是否被访问过
            visited[neighbor]=True # 如果未访问过，则标记为已访问
            dfs(graph,neighbor,visited) # 对邻居节点调用dfs，继续从该节点出发遍历剩余图

def main():
    import sys
    input=sys.stdin.read # 将标准输入内容全部读入
    data=input().split() # 将输入按照空格分割成字符串列表
    
    n=int(data[0]) # 节点数
    m=int(data[1]) # 边数
    
    graph=[[] for _ in range(n+1)] # 图的邻接表
    # graph[i]：节点i的邻居节点列表
    # n+1：从节点编号1开始，避免混淆
     
    index=2 # 从data[2]开始处理边的信息
    for _ in range(m): # 遍历每条边
        # 从输入数据中读取一条边的起点s和终点t
        s=int(data[index]) 
        t=int(data[index+1])
        # 在邻接表中记录从s到t的有向边
        graph[s].append(t)
        # 更新索引，指向下一条边的数据
        index+=2
    
    # 初始化visited
    visited=[False]*(n+1)
    # 标记节点1为已访问
    visited[1]=True
    # 从1开始深度优先搜索
    dfs(graph,1,visited)
    
    # 连通性检查
    for i in range(1,n+1):
        if not visited[i]: # 检查节点i是否未访问过
            # 如果有节点未访问过，说明从节点1出发无法遍历整个图，输出-1
            print(-1)
            return
    # 所有节点均可访问，输出1  
    print(1)

# 调用主程序
if __name__=='__main__':
    main()
    
# prim三部曲：
# 1. 选距离生成树最近节点
# 2. 最近节点加入生成树
# 3. 更新非生成树节点到生成树的距离（更新minDist数组）
# minDist数组用来记录每个节点距离最小生成树的最近距离

# prim算法：
# 1.从图中任意选择一个顶点作为起始点，将其加入到已选顶点集合中；
# 2. 每次从已选顶点集合相邻的边种，选择一条权值最小的边，将这条边以及它所连接的未选点加入到已选顶点集合和最小生成树的边集合中
# 3. 重复上述步骤，直到所有顶点都已经被加入到已选顶点集合中。此时得到的边集合和所有顶点就构成了最小生成树

# 时间复杂度：O(v^2)
# 1. 初始化邻接矩阵：O(v^2)
# 2. 填充邻接矩阵：O(e)
# 3. 初始化minDist和visited数组：O(V)
# 4. prim算法主循环：外层循环执行v-1次，内层循环执行v次，O(V^2)
# 5. 统计结果：O(v)

# 空间复杂度：O(v^2)
# 1. 邻接矩阵：O(v^2)
# 2. minDist数组：O(v)
# 3. visited数组：O(v)
# 4. edges列表：O(e)



def prim(v, e, edges): # v是顶点数，e是边数，edges是存储的边的集合和值
    # 初始化邻接矩阵
    grid=[[10001]*(v+1) for _ in range(v+1)]

    # 读取边的信息填充邻接矩阵
    for edge in edges:
        # 这是一个无向图
        x, y, k=edge
        grid[x][y]=k
        grid[y][x]=k
    
    # 记录每个节点到最小生成树的最近距离
    minDist=[10001]*(v+1)

    # 记录每个节点是否已经加入到最小生成树中，初始值为False
    visited=[False]*(v+1)

    # prim算法主循环，遍历节点
    for i in range(1, v):
        cur=-1 # 目前遍历的节点
        minVal=float('inf')

        # 第一个循环用于选择距离生成树最近的节点，通过遍历minDist数组找到未被访问并且距离最小的节点
        for j in range(1, v+1):
            if not visited[j] and minDist[j]<minVal:
                minVal=minDist[j]
                cur=j
        
        # 将最近的节点加入生成树
        visited[cur]=True

        # 第二个循环用于更新非生成树节点到生成树的距离，遍历所有未被访问的节点，如果当从前节点到该节点的距离小于之前记录的距离，则更新minDist数组
        for j in range(1, v+1):
            if not visited[j] and grid[cur][j]<minDist[j]:
                minDist[j]=grid[cur][j]
    
    # 统计结果
    result=sum(minDist[2:v+1]) # 排除了minDist[0]（未被使用）和minDist[1]（起始点，没有边信息）
    return result

def main():
    # 接受输入
    # v是顶点数，e是边数
    v, e=map(int, input().split())

    edges=[]
    for _ in range(e):
        x, y, k=map(int, input().split())
        edges.append((x, y, k))
    
    result=prim(v, e, edges)
    print(result)

if __name__=='__main__':
    main()
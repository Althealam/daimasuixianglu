# 时间复杂度：
# 1. 深度优先搜索遍历所有路径：每次递归都会访问一个新的节点，最多会访问n层节点。对于每个节点，内层循环会检查从该节点出发的所有可能边（最多n条）
# 2. 处理边信息：构建邻接矩阵时需要读取m条边，复杂度为O(m)
# 总的时间复杂度：O(n*n!+m)
# 空间复杂度：
# 1. 递归调用栈：递归调用深度最多为n，每次调用需要存储当前节点的状态，复杂度为O(n)
# 2. 邻接矩阵存储：存储nxn的邻接矩阵，复杂度为O(n^2)
# 3. 路径与结果存储：path动态存储当前路径，大小最多为O(n)；result存储所有路径，最坏情况下存储O(n!)

def dfs(graph,x,n,path,result):
    """利用深度优先搜索在有向图中寻找从节点1到节点n的所有路径"""
    """
        graph: 邻接矩阵表示的图
        x：当前遍历到的节点
        n：目标节点的编号
        path：当前路径（动态记录访问节点的顺序）
        result：保存所有找到的路径的列表
    """
    if x==n:
        result.append(path.copy())
        return
    for i in range(1,n+1):
        # 如果存在一条边x->i（即graph[x][i]==1，表示从当前节点可以前往i，将节点i添加到当前路径）
        # 寻找x到i的路径，如果存在的话，就讲i加入path中
        if graph[x][i]==1:
            path.append(i)
            # 回溯
            # 寻找到i的路径
            dfs(graph,i,n,path,result)
            path.pop()

def main():
    """
    读取输入并构建邻接矩阵graph
    """
    # n是节点数，m是边数
    n,m=map(int,input().split())
    # 邻接矩阵是n+1行n+1列的
    graph=[[0]*(n+1) for _ in range(n+1)]
    
    for _ in range(m):
        s,t=map(int,input().split())
        graph[s][t]=1
    
    result=[]
    dfs(graph,1,n,[1],result)
    
    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str,path)))

if __name__=='__main__':
    main()
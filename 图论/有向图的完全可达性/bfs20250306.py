# 时间复杂度：O(n^2+k)
# 1. 输入处理部分：O(n^2+k)
# 2. BFS遍历部分：O(n+k)
# （1）每个节点最多会出队和入队一次，总共n个节点 O(n)
# （2）每条边最多会被检查一次：O(k)
# 3. 结果判断：O(n)

# 空间复杂度：O(n^2)
# 1. 相邻矩阵grid：O(n^2)
# 2. 访问数组visited：O(n)
# 3. 队列：O(n)

from collections import deque
def main():
    # 处理输入数据
    n, k=map(int, input().split())

    grid=[[0]*n for _ in range(n)]

    for _ in range(k):
        s, t=map(int, input().split())
        grid[s-1][t-1]=1

    visited=[False]*n # 记录是否遍历到该节点

    visited[0]=True # 第一个节点一定是遍历过的
    bfs(grid, 0, visited) # 开始遍历有向图，获取visited矩阵

    # 如果有没遍历过的节点，那么就直接返回-1
    for i in range(n):
        if not visited[i]:
            print(-1)
            return
    # 如果所有节点都遍历过了，则直接返回1
    print(1)


def bfs(grid, key, visited):
    queue=deque([key])
    while queue:
        key=queue.popleft()
        for i in range(len(grid[key])):
            # 如果从key到i有边并且i节点未被访问过
            if grid[key][i]==1 and not visited[i]:
                visited[i]=True
                queue.append(i)


if __name__=='__main__':
    main()
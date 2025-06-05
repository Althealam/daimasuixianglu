# 并查集：两个节点是否在同一个集合中
# 1. 寻找根节点：判断该节点的祖先节点是什么
# 2. 将两个节点加入到同一个集合中
# 3. 判断两个节点是否在同一个集合中

n, m = map(int, input().split())
# n为节点个数，m为边的个数

class UnionFind:
    def __init__(self, size):
        self.parent=list(range(size+1))
    def find(self, u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            self.parent[root_v]=root_u
    def is_same(self, u, v):
        return self.find(u)==self.find(v)

uf=UnionFind(n) # 创建并查集
for _ in range(m):
    s, t = map(int, input().split())
    uf.union(s, t)

source, destination = map(int, input().split())
if uf.is_same(source, destination):
    print(1)
else:
    print(0)
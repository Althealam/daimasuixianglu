# 并查集：判断图中是否存在环，计算图的连通分量个数，处理社交网络中的好友关系
# 不断的合并不同的集合，并快速的判断两个元素是否属于同一个集合
# 参考链接：https://www.runoob.com/data-structures/union-find-quick-merge.html
# 思路：如果一条边连接的两个节点已经在同一连通分量里，那就有环；如果所有边都处理完了也没出现这种情况，那就说明图里没有环


# 1. 初始化：将每个元素看做一个独立的集合，即每个元素的父节点是他自己
n=5 # 元素个数
father=[i for i in range(n)] # 父节点集合

# 2. 查找：确定某个元素所属的集合（找到该元素所在集合的根节点）
def find(u):
    if u==father[u]:
        return u
    else:
        return find(father[u])

# 3. 合并：将两个不同的集合合并为一个集合（将一个集合的根节点的父节点设置为另一个集合的根节点）
def union(u, v):
    root_u=find(u) # u的根节点
    root_v=find(v) # v的根节点
    if root_u!=root_v: # 把u的根节点的父节点设置为v的根节点
        father[root_u]=root_v
        return False
    # 说明u和v属于同一个集合，即它们处于同一个连通分量中，此时添加边(u,v)会形成一个环
    elif root_u==root_v: # 存在环
        return True

# 3. 边的信息
edges=[(0,1), (1,2), (2,3), (3,4), (4,0)]
has_cycle=False # 是否有环
for u, v in edges:
    if union(u, v):
        has_cycle=True
        break

if has_cycle:
    print("图中存在环！")
else:
    print("图中不存在环！")

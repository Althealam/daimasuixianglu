# kruskal算法思路：
# 1. 边的权重排序，优先选择最小的边加入到生成树中
# 2. 遍历排序后的边
# （1）如果边首尾的两个节点在同一个集合，说明如果连上这条边图中会出现环
# （2）如果边首尾的两个节点不在同一个集合，加入到最小生成树，并把两个节点加入到同一个集合

# 时间复杂度：O(eloge)
# 1. 边排序操作：O(eloge)
# 2. 并查集初始化：O(v)
# 3. 遍历边并进行并查集操作：O(e)
# 4. 计算总权重：O(v)

# 空间复杂度：O(e+v)
# 1. 存储边的信息：O(e)
# 2. 并查集相关数组：O(v)
# 3. 存储最小生成树的边的列表：O(v)

# 代码整体思路：
# 1. 边排序：将图中所有的边按照权值大小从小到大排序
# 2. 初始化并查集：为图中的每个顶点创建一个独立的集合，使用并查集来管理这些集合
# 3. 选择边：依次遍历排序后的边，若边的两个端点不在同一个集合中，则将这条边加入最小生成树，合并这两个端点所在的集合
# 4. 结束条件：当最小生成树中的边数达到顶点数-1的时候，算法结束
# 5. 计算总权值：将最小生成树中所有边的权值相加，得到最小生成树的总权值

def find(parent, i):
    """
    查找节点i所在集合的代表元素
    """
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    """
    合并两个不想交的集合。
    通过比较两个集合的rank，将rank较小的集合合并到rank较大的集合中
    """
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(v, e, edges):
    result = []

    # 按照边的权重值进行排序
    edges.sort(key=lambda x: x[2])

    parent = []  # 存储每个节点的父节点
    rank = []
    for node in range(v + 1):
        parent.append(node)
        rank.append(0)

    e_count = 0  # 已加入最小生成树的边的数量
    i = 0  # 遍历的边的索引
    while e_count < v - 1 and i < len(edges):
        x, y, w = edges[i]

        # 寻找其父节点
        set_x = find(parent, x)
        set_y = find(parent, y)

        if set_x != set_y:
            e_count += 1
            result.append((x, y, w))
            union(parent, rank, set_x, set_y)
        i += 1

    total_weight = sum([w for _, _, w in result])
    return total_weight


def main():
    v, e = map(int, input().split())

    edges = []
    for _ in range(e):
        v1, v2, val = map(int, input().split())
        edges.append((v1, v2, val))

    result = kruskal(v, e, edges)

    print(result)

if __name__ == '__main__':
    main()
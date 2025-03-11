from collections import defaultdict

father = list()  # 定义父节点集合

def find(u):
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])
        return father[u]

def is_same(u, v):
    u = find(u)
    v = find(v)
    return u == v

def join(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        father[u] = v

def is_tree_after_remove_edge(edges, edge, n):
    # 初始化并查集
    global father
    # 假设每个节点的父节点都是自己
    father = [i for i in range(n + 1)]

    for i in range(len(edges)):
        if i == edge:
            continue
        s, t = edges[i]
        if is_same(s, t):  # 成环，即不是有向树
            return False
        else:  # 将s和t放入集合中
            join(s, t)
    return True

def get_remove_edge(edges, n):
    global father
    father = [i for i in range(n + 1)]
    for s, t in edges:
        if is_same(s, t):
            print(s, t)
            return 
        else:
            join(s, t)

if __name__ == '__main__':
    n = int(input())
    edges = list()
    in_degree = defaultdict(int)

    for i in range(n):
        s, t = map(int, input().split())
        in_degree[t] += 1  # 记录其入度
        edges.append([s, t]) 

    # 寻找入度为2的边，并记录其下标
    vec = list()
    for i in range(n - 1, -1, -1):
        if in_degree[edges[i][1]] == 2:
            vec.append(i)

    # 输出
    if len(vec) > 0:
        # 情况1：删除输出顺序靠后的边
        if is_tree_after_remove_edge(edges, vec[0], n):
            print(edges[vec[0]][0], edges[vec[0]][1])
        else:
            # 情况2：只能删除特定的边
            print(edges[vec[1]][0], edges[vec[1]][1])
    else:
        # 情况3：图中有环
        get_remove_edge(edges, n)
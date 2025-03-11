# 并查集：判断两个元素是否在同一个集合中
# 并查集的功能：（1）将两个元素添加到一个集合中（2）判断两个元素在不在同一个集合中

# 时间复杂度：O(n)
# 1. 初始化father：O(n)
# 2. 查找操作：find O(1)
# 3. 合并操作：O(1)
# 4. 寻找冗余边：O(n)

# 空间复杂度：O(n)
# 1. father列表：需要存储每个节点的父节点，O(n)
# 2. 其他变量：O(1)

# 思路：
# 在一个包含n个节点的无向连通图里，正常情况下有n-1条边就可以使得图连通。当边的数量超过n-1条的时候，就会存在冗余边，也就是去掉这条边后图依然保持连通。

father=list()
# 存储每个节点的父节点，初始时每个节点的父节点是他自己

def find(u):
    # 查找节点u所在集合的代表元素（根节点）
    if u==father[u]:
        # 如果u等于他的父节点father[u]，说明u就是根节点
        return u
    else:
        # 通过递归调用find来查找father[u]的根节点
        father[u]=find(father[u])
        return father[u]
    

def is_same(u, v):
    # 判断两个节点是否在同一个集合中
    u=find(u)
    v=find(v)
    # 分别调用find函数来查找u和v所在集合的根节点
    # 比较两个根节点是否相同，如果相同则说明u和v在同一个集合中，返回True
    return u==v

def join(u, v):
    # 如果两个根节点不相等，说明u和v不在同一集合中，将u所在集合的根节点的父节点设置为v所在集合的根节点，实现两个集合的合并
    u=find(u)
    v=find(v)
    if u!=v:
        father[u]=v

if __name__=='__main__':
    n=int(input())
    for i in range(n+1):
        father.append(i)
    
    # 寻找冗余边
    result=None
    for i in range(n):
        s, t=map(int, input().split())
        # 判断s和t是否在同一集合中
        # 如果在同一个集合中，说明这条边是一个冗余边，将结果记录为result
        if is_same(s, t):
            result=str(s)+' '+str(t)
        else:
            join(s,t)

    print(result)
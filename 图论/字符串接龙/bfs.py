# 分析：
# 本题需要解决的问题：1. 图中的线是如何连在一起的 2. 起点和终点的最短路径长度
# 详细分析：
# 1. 判断点与点之间的关系，需要判断是不是差一个字符，如果差一个字符就是有链接
# 2. 求起点到终点的最短路径：无向图求最短路径，用广搜最合适，广搜只要搜到了终点，一定是最短的路径

def judge(s1,s2):
    # 判断两个字符串是否只差一个字符
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1
    

if __name__=='__main__':
    n=int(input()) # 字符串数量
    beginstr,endstr=map(str,input().split()) # 起点和终点字符串
    
    # 如果起点等于终点，直接返回步数为0
    if beginstr==endstr:
        print(0)
        exit()
        
    strlist=[]
    for i in range(n):
        strlist.append(input()) # 输入字符串列表
    
    # 初始化BFS队列
    visit=[False for i in range(n)]
    queue=[[beginstr,1]] # 当前字符串和步数
    while queue:
        str,step=queue.pop(0)
        
        # 如果当前字符串与终点字符串只差一个字符
        if judge(str,endstr):
            print(step+1)
            exit()
        
        # 遍历字符串列表，寻找与当前字符串可以连通的未访问字符串
        for i in range(n):
            if visit[i]==False and judge(strlist[i],str):
                visit[i]=True
                queue.append([strlist[i],step+1])
    print(0)

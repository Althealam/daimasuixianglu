# 时间复杂度：O(n^2m)
# n是字符串列表的长度，m是每个字符串的长度
# 1. 初始化部分，需要处理输入的字符串：O(n)
# 2. BFS搜索部分：O(n^2*m)
# （1）外层的while循环最多执行n次 O(n)
# （2）每次取出元素后会用judge函数进行判断，O(m)
# （3）内层for循环遍历字符串列表，O(n)

# 空间复杂度：O(nm)
# 1. 存储字符串列表：strlist O(nm)
# 2. BFS队列：queue可以存储所有的中间状态，队列占用的最多空间是O(nm)（n个字符串，每个字符串的长度为m）
# 3. 访问标记列表：O(n)

def main():
    # 处理输入
    n=int(input()) # 字符串的数量为n
    beginstr, endstr=map(str, input().split()) 
    # 起始字符串为beginstr，目标字符串为endstr

    # 处理特殊情况
    if beginstr==endstr:
        print(0)
        exit() # 结束程序
    
    # 处理输入的字符串
    strlist=[]
    for i in range(n):
        strlist.append(input())
    
    # 广度优先搜索部分
    
    # 标记字符串列表strlist中的每个字符串是否已经被访问过
    visit=[False]*n

    # 初始化队列，队列中的每个元素是一个列表，包含当前字符串和从起始字符串到当前字符串的步数
    queue=[[beginstr, 1]]


    while queue:
        # 从队列头部取出当前字符串和对应的步数
        cur_str, step=queue.pop(0)
        
        # 判断当前字符串是否和目标字符串是否只是有一个字符不同
        # 如果是的话，那么只需要修改一个字符即可
        if judge(cur_str, endstr):
            print(step+1)
            exit()
        
        # 如果当前字符串和目标字符串有超过1个字符不同
        for i in range(n):
            if visit[i]==False and judge(strlist[i], cur_str):
                # 将该字符串标记为已度
                visit[i]=True 
                queue.append([strlist[i],step+1])
    print(0)


def judge(s1, s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    if count==1:
        return True
    return False

if __name__=='__main__':
    main()
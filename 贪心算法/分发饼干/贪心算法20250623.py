# 思路：用最小的饼干去满足胃口最小的孩子，如果发现这个小饼干不能满足该孩子，则跳到下一个孩子

# 
g = list(map(int, input().split())) # 胃口值
s = list(map(int, input().split())) # 饼干的尺寸

def greedy(g, s):
    g.sort() # 孩子的胃口值
    s.sort() # 饼干的尺寸
    res = 0 # 满足的孩子个数
    for i in range(len(s)): # 遍历饼干
        if res>=len(g): # 孩子已经分完了
            return res
        if res<len(g) and s[i]>=g[res]: # 饼干满足胃口
            res+=1
    return res
        

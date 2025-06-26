# 思路：
# 1. 统计每个字符最后出现的索引
# 2. 从头遍历字符串，获取当前字符的最远出现下标，如果i到达了最远下标，则到达了分割点，更新: res.append(end-start+1) start=end+1
# 每次遍历的时候获取每个字符的最远出现下标：end = max(end, hash_map[S[i]])
S = str(input())

def greedy(S):
    # 1. 获取每个字符的最远出现索引
    hash_map = {}
    for i in range(len(S)):
        hash_map[s[i]]=i

    # 2. 从头遍历字符串，更新字符的最远出现下标
    res = []
    start = 0
    end = 0
    for i in range(len(S)):
        end = max(end, hash_map[S[i]])
        if i==end:
            res.append(end-start+1)
            start = end+1
    return res
result = greedy(S)
print(result)

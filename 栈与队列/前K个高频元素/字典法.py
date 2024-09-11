# 思路：使用大顶堆和小顶堆
# 大顶堆和小顶堆底层是一个二叉树
# 大顶堆指的是头部的元素都要比孩子的元素大（根节点是最大的）
# 小顶堆指的是头部的元素都要比孩子的元素小（根节点是最小的）
# 利用map存储nums里所有元素出现的频次，k为nums的值，value为出现的次数
# 我们应该利用小顶堆来找前k个高频的元素
# 为什么不适用大顶堆？定义一个大小为k的大顶堆，在每次移动更新大顶堆的时候，每次弹出都把最大的元素弹出去了，那么没办法保留下来前k个高频元素
# 我们使用小顶堆，因为要统计前k个元素，只有小顶堆每次将最小的元素弹出，然后小顶堆里积累的才是前k个最大元素


# 分析：
# 1. 要统计元素出现频率
# 2. 对频率排序
# 3. 找出前k个高频元素

# 时间复杂度：O(nlogn)
# 1. 统计数字出现次数：O(n)
# 2. 根据出现次数分组：O(m) m是不同数字的数量，最坏情况下为O(n)
# 3. 排序出现次数：key.sort()需要对出现次数进行排序，时间复杂度为O(mlogm)
# 4. 获取前k项：while key and cnt!=k: O(m)
# 总的时间复杂度为O(n+mlogm+m) 简化为O(nlogn)
# 空间复杂度：O(n+k)
# 1. 统计数字出现次数：time_dict字典存储了所有数字以及其出现次数O(m)
# 2. 根据出现次数分组：index_dict字典存储了每个出现次数对应的数字集合 O(m)
# 3. 排序出现次数：排序操作本身不需要额外的空间
# 4. 结果列表：result列表存储了最终的前k个高频数字，空间复杂度为O(k)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 使用字典统计数字出现次数
        time_dict=defaultdict(int) # 使用collections的defaultdict类创建了一个默认值为整数-的字典
        for num in nums: # 遍历nums中的每个数字，对于每个数字num，将其在time_dict中的计数加1
            time_dict[num]+=1

        # 更改字典，key为出现次数，value为相应的数字的集合
        index_dict=defaultdict(list) # 创建另一个默认值为列表的字典index_dict，用于根据数字的出现次数将数字分组
        for key in time_dict: # 遍历time_dict字典中的每个键（即nums中的每个数字）
            index_dict[time_dict[key]].append(key) # 将每个数字key加到index_dict字典中，以它出现的次数为键
        
        # 排序
        key=list(index_dict.keys()) # 获取index_dict字典中的所有键（即所有不同的出现次数），并且转换为列表
        key.sort() # 对出现次数进行排序，这样key中的元素就是从低到高的顺序
        result=[] # 初始化一个空列表，存储最终的前k个高频数字
        cnt=0 # 初始化一个计数器，用于跟踪已经添加到result列表中的数字数量
        # 获取前k项
        while key and cnt!=k: # 使用一个循环来遍历所有出现次数列表
            result+=index_dict[key[-1]] # 将当前出现次数下的所有数字添加到result列表中
            # key[-1]表示当前遍历到的出现次数列表的最后一个元素，即最大的出现次数
            cnt+=len(index_dict[key[-1]]) # 更新计数器cnt，加上当前出现次数下所有数字的数量
            key.pop() # 从出现次数列表中移除当前遍历到的最大出现次数
        
        return result[0:k] # 返回result列表中的前k个元素
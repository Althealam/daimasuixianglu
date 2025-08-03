import heapq
# 注意：heapq仅仅实现小顶堆，如果需要最大堆的话需要插入元素的负值来实现

# 1. heappush(heap, item)：向堆中插入一个元素，并且保持小顶堆的性质（堆顶元素是最小值）
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heap)

# 2. heappop(heap)：移除并返回堆顶元素（最小值），同时自动调整堆结构
print(heapq.heappop(heap)) # 移除堆顶元素1
print(heap)

# 3. heapify(list)：将一个普通列表原地转换为堆（小顶堆）
arr = [3,1,2,5,4]
heapq.heapify(arr)
print(arr)

# 4. heappushpop(heap, item)：先插入元素item，再删除并返回堆顶元素
heap = [1,3,2]
print(heapq.heappushpop(heap, 0)) # 插入0后，堆顶元素变为0，返回0
print(heap)

# 5. heapreplace(heap, item)：先删除并返回堆顶元素，再插入item
heap = [1,3,2]
print(heapq.heapreplace(heap, 0)) # 先删除堆顶1，再插入0，返回1
print(heap)

# 6. nlargest(n, iterable)和nsmallest(n, iterable)：返回可迭代对象中前面n个最大或者最小的元素
arr = [3,1,4,1,5,9]
print(heapq.nlargest(2, arr))
print(heapq.nsmallest(2, arr))
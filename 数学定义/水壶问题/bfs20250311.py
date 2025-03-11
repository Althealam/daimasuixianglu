import collections
class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :param x：水壶A的容量
        :param y：水壶B的容量
        :param z：目标
        """

        if z<0 or x+y<z:
            return False

        # BFS
        q=collections.deque([(0,0)]) # (0,0)表示水壶A和水壶B中的容量初始为0
        visited=set({(0,0)}) # 当前访问过的节点
        
        while q:
            # current node processing
            a, b=q.popleft() # 取出当前水壶内的容量

            if a==z or b==z or a+b==z:
                return True

            # generate other nodes
            states=self._gen_states(a, b, x, y)

            # check visited, push node->queue
            for state in states:
                if state not in visited:
                    visited.add(state)
                    q.append(state)

        return False

    def _gen_states(self, a, b, x, y):
        """
        :param a: 当前水壶A的体积
        :param b: 当前水壶B的体积
        :param x: 当前水壶A的最大容量
        :param y: 当前水壶B的最大容量
        """
        states=[] # 初始化水壶A和水壶B的状态

        # 1. A和B分别清空
        states.append((0, b))
        states.append((a, 0))

        # 2. A和B分别填满水
        states.append((x, b))
        states.append((a, y))

        # 3. A->B
        # 现在水的总量是a+b
        if a+b<y:
            states.append((0, a+b))
        else:
            states.append((a+b-y, y))
        
        # 4. B->A
        if a+b<x:
            states.append((a+b, 0))
        else:
            states.append((x, a+b-y))


        return states


if __name__=='__main__':
    sol=Solution()

    print(sol.canMeasureWater(3, 5, 4))

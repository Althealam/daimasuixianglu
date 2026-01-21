class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        length = 0
        count = {}
        for right in range(len(fruits)):
            if fruits[right] not in count:
                count[fruits[right]]=1
            else:
                count[fruits[right]]+=1
            
            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            length = max(length, right-left+1)
        return length

            
#from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #c = Counter(arr)
        c = {}
        for elem in arr:
            if elem not in c:
                c[elem] = 1
            else:
                c[elem] += 1
        return len(set(c.values())) == len(c.values())
        
        
        
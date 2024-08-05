class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count_dist = {}
        for elem in arr:
            if elem in count_dist:
                count_dist[elem] += 1
            else:
                count_dist[elem] = 1
                
        #print(count_dist)
        
        i = 0
        for string_val,v in count_dist.items():
            if v == 1:
                i +=1
                #print(string_val,v,i)
                if i == k :
                    return string_val
        return ""
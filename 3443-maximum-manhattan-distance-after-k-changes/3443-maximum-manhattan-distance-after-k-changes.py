class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        #aproach O(n) ?
        #make hash_s, change opsotive of max:
        #nooooo, because is on order 

        #calculate manhattan position for each ch in s and add mim(k,max_contra):

        
        hash_s  = {'N':0,'S':0,'E':0,'W':0}
        max_dist = 0
        for ch in  s:
            hash_s[ch] +=1
            min_x = min(hash_s['E'],hash_s['W'])
            kx = min(k,min_x)
            max_x = max(hash_s['E'],hash_s['W'])+2*kx-min_x

            min_y = min(hash_s['N'],hash_s['S'])
            ky = min(k-kx,min_y)
            max_y = max(hash_s['N'],hash_s['S'])+2*ky-min_y

            curr_max_dist = max_x + max_y
            max_dist = max(max_dist,curr_max_dist)

            #print(hash_s,(min_x,max_x,kx),(min_y,max_y,ky),curr_max_dist,max_dist )
        return max_dist


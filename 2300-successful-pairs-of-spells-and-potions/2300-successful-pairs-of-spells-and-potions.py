class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        #sort potions
        #use bisection to find_potion = ceil( success/ spell_i) 

        n = len(spells)
        m = len(potions)

        def bisect(x):
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if potions[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l if l < m else - 1

        potions.sort()
      
        ans = [0]*n
        for i,spell in enumerate(spells):          
            curr_cnt = bisect( math.ceil(success/spell) )
            if curr_cnt >= 0:
                ans[i] = m-curr_cnt

        return ans

        




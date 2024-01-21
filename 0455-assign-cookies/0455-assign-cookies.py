class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        s_pointer_size_cookie = 0
        num_cookies_s = len(s)
        
        for n_happy_kids,g_kid_greed in enumerate(g):
            while s_pointer_size_cookie < num_cookies_s and g_kid_greed > s[s_pointer_size_cookie]:
                s_pointer_size_cookie +=1
            if s_pointer_size_cookie == num_cookies_s:
                return  n_happy_kids
            s_pointer_size_cookie +=1
        
        return  n_happy_kids+1
            
        

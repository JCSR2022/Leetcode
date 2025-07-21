class Solution:
    def makeFancyString(self, s: str) -> str:
        
        cnt = 0
        ans = ""
        prev = ""
        for ch in  s:
            if ch == prev:
                cnt += 1
            else:
                cnt = 0
            prev = ch
            if cnt < 2:
                ans += ch
            
        return ans
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  #-------------------------------------------------------------
        #brute force
        
        # ans = ""
        # ch_val = ""
        # ch_count = 0
        # for ch in s:
        #     if ch_val == ch:
        #         ch_count += 1
        #         if ch_count < 2: 
        #             ans +=ch    
        #     else:
        #         ch_count = 0
        #         ch_val = ch
        #         ans +=ch
                
        # return ans
    
                
                    
                    
        
        
class Solution:
    def maxOperations(self, s: str) -> int:
        

        current_ones = s.count("1")
        total_moves = 0
        prev_one = True    
  
        for i in range(len(s)-1,-1,-1):
            #print(i,"ini:",prev_one,s[i],current_ones,total_moves)
            if not prev_one:
                if s[i] == "1":
                    prev_one = True
                    current_ones -=1
                continue

            if s[i] == "0" :
                total_moves += current_ones
                prev_one = False
            else:
                current_ones -=1
                
            #print(i,"fin:",prev_one,s[i],current_ones,total_moves)
        
        return total_moves

  
  
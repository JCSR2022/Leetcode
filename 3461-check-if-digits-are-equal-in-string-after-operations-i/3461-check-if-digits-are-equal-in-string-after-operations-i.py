class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        curr_s = [ int(ch) for ch in s]
        curr_size = len(curr_s) 
        
        while curr_size > 2:
            new_curr = []
            for i in range(1,curr_size):
                new_curr.append((curr_s[i-1]+curr_s[i])%10 )

            curr_size -=1
            curr_s = new_curr

        return curr_s[0] == curr_s[1]

        
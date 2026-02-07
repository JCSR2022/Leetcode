class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        
        #brute force:
        #two pointers l, r:
        # pointer l move from left to rigth, counts "b" to the left
        # pointer r move from right to lefth, count "a" on the right
        # create sum_ab with sum of count, return min
        
        sum_ab = [0]*len(s)
        count_a = 0
        count_b = 0
        for l in range(len(s)):
            r = len(s)-l-1
            
            if s[l] == 'b': count_b +=1
            if s[r] == 'a': count_a +=1
    
            sum_ab[l] += count_b
            sum_ab[r] += count_a
            #print(l,r,s[l],s[r],count_b,count_a)
        #print(sum_ab)
            
        return min(sum_ab)-1
        
        
        
class Solution:
    def minimumDeletions(self, s: str) -> int:
        

        #only 2 pass

        sum_a = [0]*(len(s)+1)

        for i in range(len(s)-1,-1,-1):
            sum_a[i] = sum_a[i+1]
            if s[i] =='a':
                sum_a[i] += 1

        ans = len(s)
        count_b = 0
        for i in range(len(s)):
            if s[i] == 'b':
                count_b += 1
        
            ans = min(ans,sum_a[i]+count_b)
        
        return ans-1







#-----------------------------------------------------------    
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
            print(sum_ab,l,count_a,count_b)
            #print(l,r,s[l],s[r],count_b,count_a)
        #print(sum_ab)
            
        return min(sum_ab)-1
        
#-------------------------------------------------------
# #just to visualize:

        
#         sum_a = [0]*len(s)
#         sum_b = [0]*len(s)
#         count_a = 0
#         count_b = 0
#         for l in range(len(s)):
#             r = len(s)-l-1
            
#             if s[l] == 'b': count_b +=1
#             if s[r] == 'a': count_a +=1
    
#             sum_a[r] += count_a
#             sum_b[l] += count_b
#             print(sum_b,sum_a)
            
#         sum_ab = [a+b  for a,b in zip(sum_a,sum_b)]
#         print(sum_b)
#         print(sum_a)
#         print(sum_ab)
#         return min(sum_ab)-1
        
        
        
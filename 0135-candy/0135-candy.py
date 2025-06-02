class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # ratings = [ratings[0]]+ratings+[ratings[-1]]
        # n = len(ratings)
        # candies = [1]*n
        
        # i = 1
        # j = 2
        # while j < n-1:
        #     if  ratings[i] < ratings[j]:
        #         candies[i+1] = candies[i]+1      
        #         i+=1
        #         j+=1
        #     elif ratings[i] == ratings[j]:
        #         candies[i+1] = candies[i]      
        #         i+=1
        #         j+=1
        #     else:
        #         new_i = i
        #         new_j = j
        #         cnt = 0
        #         while ratings[new_i] > ratings[new_j] and new_j < n :
        #             cnt +=1
        #         while  cnt>0:


        # ans = sum(candies[1:-1]) 

#----------------------------------------------------
    #[1,2,5,4,3,1,0,2]

    #   return sum([1,2,5,4,3,2,1,2])


#------------------------------------------------------------------
#         #[1,0,2,2,3]
#         # [2,1,2,1,2]

#         ratings = [ratings[0]]+ratings+[ratings[-1]]
#         n = len(ratings)
#         candies = [1]*n
#         print(ratings)

#         for i in range(1,n-1):
#             # if ratings[i]>ratings[i-1] or ratings[i]>ratings[i+1]:
#             #    candies[i] = max(candies[i-1],candies[i+1])+1
#             if ratings[i]>ratings[i-1]:
#                 candies[i] = candies[i-1]+1
            
#             if ratings[i] == ratings[i-1]:
#                 candies[i] = candies[i-1]
            
#             if ratings[i]>ratings[i+1]:
#                 candies[i] = candies[i+1]+1
            
#             print(ratings[i],candies)

#         return sum(candies) - 2
# no imbecil!!!!!!!!!
#---------------------------------------------------------------














#------------------------------------------------------
        size = len(ratings)
        
        if size == 1:
            return 1
    
        if size == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
            
       # size > 2
        candies = [1]*size
        for i in range(1,size):
            if ratings[i -1] < ratings[i]:
                candies[i] = candies[i-1] + 1
                
        for i in range(size-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1]+1)
        return sum(candies)
        
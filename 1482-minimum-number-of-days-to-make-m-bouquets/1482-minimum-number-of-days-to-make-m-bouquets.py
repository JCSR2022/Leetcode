class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
                if total >= m:
                    return True
            return False
        
        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1
        
        return low
        
    
    
    
    
    
#         #lijnblakwjblkdafFQEifdakfokslbNFsbvda
#         #vete aa= la maldit a moias;nofwnkfd;lsnosagr;lnkgfvb'sfnklnfKSD:Lvnfs'lkmwv\]
#         #we":l,sd;snlmn;lkngkvnzflknb ahbmgtrz:B
        
#         #Binary search for days0

#         if m*k> len(bloomDay):
#             return -1
        
#         def isPos_mGroups_k(days):
#             count_k = 0
#             count_m = 0
#             for n in bloomDay:
#                 #print(m,n <= days,n,days,count_k,count_m,count_k // k)
#                 if n <= days:
#                     count_k += 1
#                 else:
#                     count_m += count_k // k 
#                     count_k = 0
#                     if count_m >= m:
#                         return True
                    
#             count_m += count_k // k 
#             #print('maskjz mck:',count_m,m ,count_m >= m )
#             if count_m >= m:
#                 return True
            
#             return False
        
        
#         l = min(bloomDay)
#         r = max(bloomDay)
        
#         while l < r :
            
            
#             mid = r + (l-r)//2
#             iPos = isPos_mGroups_k(mid)
#            # print(l,r,mid,iPos)
            
#             if  iPos:
#                 r = mid-1
#             else:
#                 l = mid+1
                
#         return l
        
            
            
            
            
        
        
        
        
        
        
#         #brute force, check day by day if there m grups of k adjacent flowers
#         #brute force, do not work,  time limit exceeded
#         if m*k> len(bloomDay):
#             return -1
        
#         def isPos_mGroups_k(days):
#             count_k = 0
#             count_m = 0
#             for n in bloomDay:
#                 #print(n <= days,n,days,count_k,count_m,count_k // k)
#                 if n <= days:
#                     count_k += 1
#                 else:
#                     count_m += count_k // k 
#                     count_k = 0
#                     if count_m == m:
#                         return True
                    
#             count_m += count_k // k 
#             if count_m >= m:
#                 return True
            
#             return False
        
#         for days in range(min(bloomDay),max(bloomDay)+1):
#            # print(days,isPos_mGroups_k(days))
#             if isPos_mGroups_k(days):  
#                 return days

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brutForce2:
        #   use a window os size k and find the max days to use the floweres on that window, make arr
#         #   sort that arr, find the max val of the first m values
#         arr = []
#         for i in range(0,len(bloomDay)-k+1):
#             print(bloomDay[i:i+k])
#             arr.append(bloomDay[i:i+k])
#         adj = []
#         print(arr, arr[:m])
#         #no, because adjcent group cant be taken if take [1,2,3], cant take [2,3,4]
#         return 0
         
        
  
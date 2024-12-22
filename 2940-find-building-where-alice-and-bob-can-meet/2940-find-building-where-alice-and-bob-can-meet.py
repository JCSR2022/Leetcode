class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        #Aproach
        # use  stack
        # begin on max(queries[x])
        #no find way
#-----------------------------------------------------------------------------
        #brute force, n**2
        # for each h, creat leas of all posibles positions
        # join posibles return min , if no join -1
        
        
#         posibles = [ { (h,j+i+1) for j,h in enumerate(heights[i+1:]) if h > act_h} for i,act_h  in enumerate(heights)]
#         for i,h in enumerate(heights):
#             posibles[i].add((h,i))
            
#         #print(posibles)
        
#         ans = []
#         for a,b in queries:
#             posible_ans =  posibles[a]&posibles[b]
#             #print(a,b,posible_ans)
#             if posible_ans:
#                 h_i_ans = min(posible_ans, key=lambda x: x[1]) 
#                 ans.append(h_i_ans[1])
#             else:
#                 ans.append(-1)
        
#         return ans

#memory limit exceeded

#---------------------------------------------------------------
        #brute force #len(queries)*len(heigths)
    
#         ans = []
        
#         for q in queries:
#             l,r = sorted(q)
            
#             if l == r or heights[r]>heights[l]:
#                 ans.append(r)
#                 continue
                
#             min_h = max(heights[l],heights[r])

#             fin = False
#             for j in range(r+1,len(heights)):
#                 if heights[j] > min_h:
#                     ans.append(j)
#                     fin = True
#                     break
                    
#             if not fin:
#                 ans.append(-1)
      
#         return ans
        
        
#         ans = [-1]*len(queries)
        
#         for i,q in enumerate(queries):
#             l,r = sorted(q)
            
#             if l == r or heights[r]>heights[l]:
#                 ans[i] = r
#                 continue
                
#             min_h = max(heights[l],heights[r])

#             for j in range(r+1,len(heights)):
#                 if heights[j] > min_h:
#                     ans[i] = j
#                     break
      

#         return ans
               
        
#time limit exceeded
#--------------------------------------------------


        ans = [-1]*len(queries)
        groups = defaultdict(list) #[(req_h,q_inx)] 
        
        for i,q in enumerate(queries):
            l,r = sorted(q)
            if l == r or heights[r] > heights[l]:
                ans[i] = r
            else:
                min_h = max(heights[l],heights[r])
                groups[r].append((min_h,i))
                
                
             
        min_heap = []
        for i,h in enumerate(heights):
            
            for req_h,q_inx in groups[i]:
                heapq.heappush(min_heap,(req_h,q_inx))
            
            while min_heap and h > min_heap[0][0]:
                req_h,q_inx = heapq.heappop(min_heap)
                ans[q_inx] = i
    
        return ans
    
        
        
        
        
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
#         # Aproach brute force, make all posible combinations and sorted by sum
        
#         all_comb = []
        
#         for n1 in nums1:
#             for n2 in nums2:
#                 all_comb.append([n1,n2])
            
#         all_comb_sorted = sorted(all_comb, key=lambda x: sum(x))

#         return all_comb_sorted[:k]
        
    
    
    
    
    
    
    
    
    
        # 2do aproach, heap???
        
        
        
#         res = []
#         if not nums1 or not nums2 or not k:
#             return res
        
        
#         heap = []
#         visited = set()
        
#         heapq.heappush(heap, (nums1[0]+nums2[0],0,0))
#         visited.add((0,0))
        
        
#         while k and heap:
#             print(k, heap)
#             _,i,j = heapq.heappop(heap)
#             res.append([nums1[i],nums2[j]])
        
#             if i+1 < len(nums1) and (i+1, j) not in visited:
#                 heapq.heappush(heap, (nums1[i+i]+nums2[j], i+1, j))
#                 visited.add((i+1, j))

#             if j+1 < len(nums2) and (i, j+1) not in visited:
#                 heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
#                 visited.add((i, j+1))

#             k -= 1
        
        
#         return res


        A = nums1
        B = nums2

        res = []
        pq = [(A[0]+B[0], 0, 0)]
        
        def push(i, j):
            if i < len(A) and j < len(B):
                heappush(pq, (A[i]+B[j], i, j))
        
        while pq and len(res) < k:
            _, i, j = heappop(pq)
            res.append([A[i], B[j]])
            push(i, j+1)
            if j == 0 :
                push(i+1, j)
        
        return res
        
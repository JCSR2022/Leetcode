class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # aporach


#         ans = k+1
#         while tickets[k] > 1:
#             print(tickets,ans)
            
#             count_ceros = 0
#             for i,t in enumerate(tickets):
#                 if t >= 1: 
#                     tickets[i] -=1
#                 else:
#                     count_ceros += 1          
#             ans += len(tickets)-count_ceros
            
#         print(len(tickets)-count_ceros,tickets,ans)    
#         return ans
    
#         NO FUNCINA OTRA VEZ $%^#&%&$&#^$#%


        queue = deque()
        time = 0

        for i in range(len(tickets)):
            queue.append(i)

        while queue:
            index = queue.popleft()
            tickets[index] -= 1
            time += 1

            if tickets[index] == 0 and index == k:
                return time
            if tickets[index] > 0:
                queue.append(index)

        return time


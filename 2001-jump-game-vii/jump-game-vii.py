class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #brute force , gredy (just to do it more efficiente) using a heap

        # heap = [(0,0)]
        # end = len(s)-1
        # visited = set()


        # while heap:
        #     #print(heap)
        #     position,steps = heapq.heappop(heap)
        #     i = -position

        #     if i == end:
        #         return True
            
        #     if i+minJump > end:
        #         continue
        #     minJump_limit = i+minJump
        #     maxJump_limit = min(i+maxJump,end)
        #     #print(minJump_limit,maxJump_limit)
        #     for j in range(minJump_limit,maxJump_limit+1):
        #         #print("j",j,s[j],s[j] == 0 and j not in visited)
        #         if s[j] == '0' and j not in visited:
        #             visited.add(j)
        #             heapq.heappush(heap,(-j,steps+1))
        #             #print("heap",heap)

        # return False

#Time Limit Exceeded 108 / 143 testcases passed  //steps,position = heapq.heappop(heap)
#Time Limit Exceeded 117 / 143 testcases passed  //position,steps = heapq.heappop(heap)


        # heap = [0]
        # end = len(s)-1
        # visited = set()


        # while heap:
        #     position = heapq.heappop(heap)
        #     i = -position

        #     if i == end:
        #         return True
            
        #     if i+minJump > end:
        #         continue
        #     minJump_limit = i+minJump
        #     maxJump_limit = min(i+maxJump,end)

        #     for j in range(minJump_limit,maxJump_limit+1):
        #         if s[j] == '0' and j not in visited:
        #             visited.add(j)
        #             heapq.heappush(heap,-j)
        #             #print("heap",heap)

        # return False

#--------------------------------------------------------------

        #using dp? n**2 max?????

        # size = len(s)
        # end = len(s)-1

        # dp = [False]*size
        # dp[0] = True

        # for i in range(size):
        #     if size < 100:
        #         print(dp)
        #     if dp[i] and i+minJump < end:
        #         minJump_limit = i+minJump
        #         maxJump_limit = min(i+maxJump,end)
        #         for j in range(minJump_limit,maxJump_limit+1):
        #             dp[j] = s[j] == '0'
                
        # return dp[-1]
                
##Time Limit Exceeded 
#--------------------------------------------------------------------


        # size = len(s)
        # end = len(s)-1

        # dp = [False]*size
        # dp[0] = True
        # last = 0

        # for i in range(size):
        #     if dp[i] and i+minJump < end:
        #         minJump_limit = max(i+minJump,last+1)
        #         maxJump_limit = min(i+maxJump,end)
        #         for j in range(minJump_limit,maxJump_limit+1):
        #             dp[j] = s[j] == '0'
        #             last = j
        # return dp[-1]

#tu eres un maldito inutil de mierda que no sirve para nada!!!!!!!!!!!!!!!!!!!
#muerete maldito imbecil!!!!!!!!!!!!!!!!
#----------------------------------------------------------------------------




        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable += 1

            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1

            if reachable > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]
      


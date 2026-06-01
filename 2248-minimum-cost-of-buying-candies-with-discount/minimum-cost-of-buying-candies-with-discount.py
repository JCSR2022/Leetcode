class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        # cost.sort(reverse = True)
        # return sum( cost[i]  for i in range(len(cost)) if (i+1)%3 )
        

        cost.sort(reverse = True)
        ans = 0
        for i,n in enumerate(cost):
            if (i+1)%3:
                ans += n
        return ans

        
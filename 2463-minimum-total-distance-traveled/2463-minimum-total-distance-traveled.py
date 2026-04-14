class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        

        #brute force:

        factories = []
        for p,l in factory:
            factories += [p]*l
        free_fact = [True]*len(factories)

        memo_dfs = {}
        def dfs(r,dist):
            if (r,dist) in memo_dfs:
                return memo_dfs[(r,dist)]

            if r < len(robot):
                curr_min = float("inf")
                for i,fact_disp in enumerate(free_fact):
                    if fact_disp:
                        free_fact[i] = False
                        curr_dist = abs(robot[r]-factories[i])
                        curr_min = min(curr_min, dfs(r+1,dist+curr_dist))
                        free_fact[i] = True

                memo_dfs[(r,dist)] = curr_min
                return memo_dfs[(r,dist)] 

            if r == len(robot):
                memo_dfs[(r,dist)] = dist
                return memo_dfs[(r,dist)]

        return dfs(0,0)


#Time Limit Exceeded
#---------------------------------------------------------------
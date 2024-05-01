class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
#         cache = {}

#         def helper(r, k):
#             if k == len(key):
#                 return 0
#             if (r, k) in cache:
#                 return cache[(r, k)]

#             res = float("inf")
#             for i, c in enumerate(ring):
#                 if c == key[k]:
#                     min_dist = min(
#                                     abs(r - i), # between
#                                     len(ring) - abs(r - i)) # around

#                     res = min(res, min_dist + 1 + helper(i, k + 1))

#             return res

    
#         return helper(0,0)

        # the distance between two points (i, j) on the ring
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))
        # build the position list for each character in ring
        pos = {}
        for i, c in enumerate(ring):
            if c in pos: pos[c].append(i)
            else: pos[c] = [i]
        # the current possible state: {position of the ring: the cost}
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:  # every possible target position
                next_state[j] = float('inf')
                for i in state:  # every possible start position
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)
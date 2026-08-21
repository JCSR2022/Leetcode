# class Solution:
#     def findKthSmallest(self, coins: List[int], k: int) -> int:

#         #brute force, no va a funcionar par k = 2*10**9 pero es la logica incial

#         coins.sort()
#         next_cnt = [ c for c in coins]

#         while k:
#             k -=1
#             curr_cnt = min(next_cnt)
#             curr_indx = nums.index(curr_cnt)

#         return coin_cnt[0][0]
# #no imbecil, ni siqueira puedes hacer este, como vas a hacer lo del M.C.D???
# #-------------------------------------------------------------------

from typing import List
from math import gcd

class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        useful = []

        for coin in coins:
            redundant = False

            for prev in useful:
                if coin % prev == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(coin)

        low = 1
        high = useful[0] * k

        m = len(useful)
        total_masks = 1 << m

        lcms = [1] * total_masks

        signs = [1] * total_masks

        for mask in range(1, total_masks):
            current_lcm = 1
            bits = 0

            for i in range(m):
                if mask & (1 << i):
                    current_lcm //= gcd(current_lcm, useful[i])

                    if current_lcm > high // useful[i]:
                        current_lcm = high + 1
                        break

                    current_lcm *= useful[i]
                    bits += 1

            lcms[mask] = current_lcm

            signs[mask] = 1 if bits % 2 == 1 else -1

        def count(x: int) -> int:
            result = 0

            for mask in range(1, total_masks):
                if lcms[mask] <= x:
                    result += signs[mask] * (x // lcms[mask])

            return result

        while low < high:
            mid = low + (high - low) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low










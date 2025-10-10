class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:


        multi = [0]* k  #[[] for _ in range(k) ]

        for i,num in enumerate(energy):
            if multi[i%k] + num > num:
                multi[i%k] += num
            else:
                multi[i%k] = num
            #print(i%k,multi)

        return max(multi)

        
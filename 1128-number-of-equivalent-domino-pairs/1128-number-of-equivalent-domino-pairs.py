class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        hash_domino = defaultdict(int)

        for tile in dominoes:
            tile.sort()
            hash_domino[tuple(tile)] += 1

        ans = 0
        for tiles in hash_domino.values():
            ans += math.comb(tiles,2)

        return ans 
        
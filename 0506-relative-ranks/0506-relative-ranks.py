class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # brute force:
        # copy and sort 
        # make a hash table
        
        rank_val = score.copy()
        rank_val.sort(reverse=True)
        ranks = ["Gold Medal","Silver Medal","Bronze Medal"]
        ranks = ranks + [ str(i) for i in range(4,len(score)+1)]
        
        hash_ranks = { v:r for v,r in zip(rank_val,ranks) }

        print(hash_ranks)
        
        ans = []
        for val in score:
            ans.append(hash_ranks[val] )
        return ans 
        
        
        
        
        
        
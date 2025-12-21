class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        eliminated = set()
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                w1 = "".join( ch for i,ch in enumerate(strs[row-1][:col+1]) if i not in eliminated)
                w2 = "".join( ch for i,ch in enumerate(strs[row][:col+1]) if i not in eliminated)
                #print( w1,w2,w1>w2)
                if w1 > w2:
                    eliminated.add(col)
                    #print("eliminated",eliminated )
                    break 

        return len(eliminated)
        
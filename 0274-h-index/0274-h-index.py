class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == [0]:
            return 0
        
        citations.sort(reverse=True)
        for resarch_i,citation_resarch_i in enumerate(citations):
           # print(resarch_i,citation_resarch_i)
            if citation_resarch_i <= resarch_i:
                return resarch_i
        return len(citations)
    
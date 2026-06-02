class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        


        #aproach, try all combinations?

        # land = sorted([(star,t) for star,t in zip(landStartTime,landDuration)])
        # water = sorted([(star,t) for star,t in zip(waterStartTime,waterDuration)])

        
        # def dfs(l,w):
            
        #     if l<len(land) and w <len(water):
        #         #opc1 land first
        #         t_1 = land[l][0]+land[l][1]
        #         opc1 =  max(t_1,water[w][0])+water[w][1]
                
        #         #opc1 water first
        #         t_1 = water[w][0]+water[w][1]
        #         opc2 = max(t_1,land[l][0])+land[l][1]

        #         opc3 = dfs(l+1,w)

        #         opc4 = dfs(l,w+1)

        #         return min(opc1,opc2,opc3,opc4)

        #     else:
        #         return float("inf")

        #     return dfs(0,0)

#eres un maldito imbecil que nunca va a servir para nada, suicidate imbecil!!!!!!!!
#----------------------------------------------------------------------------------


        ans = float("inf")
        for l in range(len(landStartTime)):
            for w in range(len(waterDuration)):
                ls,ld = landStartTime[l], landDuration[l]
                ws,wd = waterStartTime[w], waterDuration[w]

                if ls < ws :
                    ans = min(ans,max(ls+ld,ws)+wd)
                else:
                    ans = min(ans,max(ws+wd,ls)+ld)

        return ans





































            
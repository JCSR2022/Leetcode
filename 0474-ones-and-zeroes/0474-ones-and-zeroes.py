class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #brute force

        arr = [ (s.count("0"),s.count("1")) for s in strs ]
        size = len(arr)

        memo = {}
        def dfs(i,cnt_sub_arr,ceros,ones):
            if i == size:
                return  cnt_sub_arr

            if (i,cnt_sub_arr,ceros,ones) in memo:
                return memo[(i,cnt_sub_arr,ceros,ones)]

            opc_use = 0
            opc_no_use = 0

            #try to use:
            cnt_ceros = arr[i][0]+ceros
            cnt_ones = arr[i][1]+ones
            if cnt_ceros  <= m and  cnt_ones <=n:
                opc_use =  dfs(i+1,cnt_sub_arr+1,cnt_ceros,cnt_ones)
                   
            #try no use:
            opc_no_use = dfs(i+1,cnt_sub_arr,ceros,ones)
            
            memo[(i,cnt_sub_arr,ceros,ones)] = max(opc_use,opc_no_use)
            return memo[(i,cnt_sub_arr,ceros,ones)] 

        return dfs(0,0,0,0)




        
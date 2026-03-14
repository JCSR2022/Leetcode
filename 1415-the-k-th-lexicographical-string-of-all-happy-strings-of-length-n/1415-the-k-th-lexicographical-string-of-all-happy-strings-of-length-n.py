class Solution:
    def getHappyString(self, n: int, k: int) -> str:

#------------------13/03/2026----------------------


# num_ch = {0:'',1:'a',2:'b',3:'c'}

# opc = {0:[1,2,3],1:[2,3],2:[1,3],3:[1,2]}

# num_string = [0]

# max_comb = len(opc[0])*2**n
# while k < max_comb:
#     max_comb =  



# return "".join( [ num_ch[num] for num in num_string ] )



        total_happy = 3*2**(n-1) 
        ans = []
        choices = "abc"
        low, high = 1, total_happy

        for i in range(n):
            cur = low
            partition_size = (high- low +1) // len(choices)

            for c in choices:
                if cur <= k < cur + partition_size:
                    ans.append(c)
                    low = cur
                    high = cur + partition_size-1
                    choices = "abc".replace(c,"")
                    break
                cur += partition_size

        return "".join(ans)       


#----------------------------------------------        
        #Oproach:
        #brute force O(2**(n-1))...O(k)
      
        # if k > 3*2**(n-1) return ""

        # dfs , try to always do a,then b, then c, it will create sorted
        # stop on cont  == k


        #check are less than k happy strings of length n
        # if k > 3*2**(n-1):
        #     return ""

        # def dfs(hps):
        #     nonlocal count,ans

        #     if len(ans) >0:
        #         return 
        #     if len(hps) == n:
        #         count += 1
        #         if count == k:
        #             ans = hps
        #         return
                 
        #     if hps[-1]=="a":
        #             dfs(hps+"b")
        #             dfs(hps+"c")

        #     if hps[-1]=="b":
        #             dfs(hps+"a")
        #             dfs(hps+"c")

        #     if hps[-1]=="c":
        #             dfs(hps+"a")
        #             dfs(hps+"b")

        # ans = ""
        # if k <= 2**(n-1):
        #     count = 0
        #     dfs("a")
        # elif 2**(n-1) < k <= 2*2**(n-1):
        #     count = 2**(n-1)
        #     dfs("b")
        # else:
        #     count = 2*2**(n-1)
        #     dfs("c")

        # return ans
#----------------------------------------------------

#using arr is faster than direct strings?

        # def dfs(hps):
        #     nonlocal count,ans

        #     if len(ans) > 0:
        #         return 
        #     if len(hps) == n:
        #         count += 1
        #         if count == k:
        #             ans = hps
        #         return
                 
        #     if hps[-1] == "a":
        #             dfs(hps+["b"])
        #             dfs(hps+["c"])

        #     if hps[-1]=="b":
        #             dfs(hps+["a"])
        #             dfs(hps+["c"])

        #     if hps[-1]=="c":
        #             dfs(hps+["a"])
        #             dfs(hps+["b"])

        # ans = []
        # if k <= 2**(n-1):
        #     count = 0
        #     dfs(["a"])
        # elif 2**(n-1) < k <= 2*2**(n-1):
        #     count = 2**(n-1)
        #     dfs(["b"])
        # elif 2*2**(n-1) < k <= 3*2**(n-1):
        #     count = 2*2**(n-1)
        #     dfs(["c"])
        # else:
        #     ans = [""]
    
        # return "".join(ans)
#----------------------------------------------------------

        # def dfs(hps):
        #     nonlocal count,ans

        #     if len(ans):
        #         return 

        #     if len(hps) == n:
        #         count += 1
        #         if count == k:
        #             ans = hps.copy()
        #         return

        #     for ch in "abc":
        #         if hps[-1] != ch:
        #             hps.append(ch)
        #             dfs(hps)
        #             hps.pop()


        # ans = []
        # if k <= 2**(n-1):
        #     count = 0
        #     dfs(["a"])
        # elif 2**(n-1) < k <= 2*2**(n-1):
        #     count = 2**(n-1)
        #     dfs(["b"])
        # elif 2*2**(n-1) < k <= 3*2**(n-1):
        #     count = 2*2**(n-1)
        #     dfs(["c"])
        # else:
        #     ans = [""]
    
        # return "".join(ans)



#-----------------------------------------------------
#improve with knowledge 2**(n-1), complete tree, O(n)//
#https://www.youtube.com/watch?v=tRwXzsXJArI

        # total_happy = 3*2**(n-1) 
        # ans = []
        # choices = "abc"
        # low, high = 1, total_happy

        # for i in range(n):
        #     cur = low
        #     partition_size = (high- low +1) // len(choices)

        #     for c in choices:
        #         if cur <= k < cur + partition_size:
        #             ans.append(c)
        #             low = cur
        #             high = cur + partition_size-1
        #             choices = "abc".replace(c,"")
        #             break
        #         cur += partition_size

        # return "".join(ans)       





#--------------------------------------------------------
        # n = 1 => 3
        # a
        # b
        # c


        # n = 2 => 3*2
        # ab
        # ac
        # ba
        # bc
        # ca
        # cb

        # n = 3 => 3*2*2 => 3*2**(n-1)
        # "aba"
        # "abc"
        # "aca"
        # "acb"

        # "bab"
        # "bac"
        # "bca"
        # "bcb"
        
        # "cab"
        # "cac"
        # "cba"
        # "cbc"
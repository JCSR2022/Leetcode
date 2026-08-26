class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        #sliding window

        # ans = "2"*100
        # i = 0
        # j = 0
        # cont_ones = 0
        # while s[i] == '0' and i< len(s):
        #     j = max(i,j)    
            
        #     while  cont_ones < 3 and j<len(s):
        #         cont_ones += s[j]=='1'
        #         j +=1

        #     if j == len(s):
        #         i =len(s)
        #         break

        #     if j-i < len(ans):
        #         ans = s[i:j]
        #     elif j-i == len(ans):
        #         ans = min(ans,s[i:j] )
            
        #     cont_ones -= 1
        #     i +=1

        # if ans == "2"*100:
        #     return ""
        # else:
        #     return ans

    #nooooooooo
#------------------------------------------------



        ans = ""
        n = len(s)

        for i in range(n):

            oneCnt = 0
            cur = ""

            for j in range(i, n):

                cur += s[j]

                if s[j] == '1':
                    oneCnt += 1

                # More than k ones can never become valid again
                if oneCnt > k:
                    break

                if oneCnt == k:
                    if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                        ans = cur

        return ans
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        # if sum > num*9:
        #     return ""

        # ans = [0]*num
        # i = 0
        # curr_digit = 10
        # while sum > 0:
        #     curr_digit -= 1
        #     print(i,curr_digit,sum,sum-curr_digit,sum-curr_digit >= curr_digit,ans)
        #     while sum-curr_digit <0:
        #         print(i,curr_digit,ans)
        #         ans[i] = curr_digit
        #         sum -= curr_digit
        #         i +=1


        # return "".join([ str(i) for i in ans])

#maldito imbecil, muerete, suicidate imbecil, hazle un favor al mundo!!!!
#-------------------------------------------

        if sum > 9 * num:
            return ""

        ans = []
        # Step 2: fill every position from left to right
        for _ in range(num):
            digit = min(9, sum)   # take as much as we can, at most 9
            ans.append(str(digit))
            sum -= digit

        return "".join(ans) if sum == 0 else ""



        
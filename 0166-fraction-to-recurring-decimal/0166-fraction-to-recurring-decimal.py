class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        

        # if numerator == 0:
        #     return "0"
        
        # sign = numerator*denominator < 0
        # if sign:
        #     final_ans = "-"
        # else:
        #     final_ans = ""


        # numerator = abs(numerator)
        # denominator = abs(denominator)

        # numerator_arr = [int(n) for n in str(numerator)]
        # len_numerator = len(numerator_arr)
        # numerator_arr += [0]*10000


        # ans = []
        # curr_num  = numerator_arr[0]
        # indx = 1

        # decimal =False
        # returns = {}
        # periodic = False

        # while indx < len(numerator_arr):
        #     #print(indx,curr_num ,ans,returns)
            
        #     if curr_num >= denominator:
        #         ans.append(str(curr_num//denominator))
        #         curr_num = (curr_num%denominator)*10 
        #     else:
        #         if len(ans) > 0:
        #             ans.append("0")
        #         curr_num *= 10 
        #     curr_num += numerator_arr[indx]
            
        #     if curr_num == 0:
        #         break

        #     if decimal:
        #         if curr_num in returns:
        #             indx_parentesis = returns[curr_num]
        #             periodic = True
        #             break
        #         else:
        #             returns[curr_num] = len(ans)
            
        #     indx +=1
        #     if indx == len_numerator+1:
        #         ans.append(".")
        #         decimal = True
                
            
        # #print(indx,curr_num ,ans,returns,indx_parentesis)
        # if periodic:
        #     final_ans += "".join(ans[:indx_parentesis])+"("+"".join(ans[indx_parentesis:])+")" 
        # else:
        #     final_ans += "".join(ans)

        # if final_ans[0] == ".":
        #     final_ans = "0"+final_ans

        # return final_ans
    
#no sirvio por pendejo inutil
#----------------------------------------------------------------
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append(".")
        map_dict = {}
        while remainder != 0:
            if remainder in map_dict:
                fraction.insert(map_dict[remainder], "(")
                fraction.append(")")
                break
            map_dict[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(fraction)
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        #brute force
        
        # GCD_mem = {}        
        # def eucledianGCD(x,y):
        #     x,y = sorted([x,y])
        #     a,b = x,y
        #     if (x,y) in GCD_mem:
        #         return GCD_mem[(x,y)]

        #     while a > 1:
        #         c = b//a
        #         r = b%a
        #         #print( f" {b} = {c}*{a} + {r} " )
        #         b = a
        #         a = r

        #     GCD_mem[(x,y)] =  b if a == 0 else 1
        #     return GCD_mem[(x,y)]
                    
        # def LCD(x,y):
        #     return x*y//eucledianGCD(x,y)

        # i = 0
        # j = 1

        # while j < len(nums):
        #     x = nums[i]
        #     y = nums[j] 
            
        #     if  eucledianGCD(x,y) > 1:
        #         nums[i] = 0    
        #         nums[j] = LCD(x,y)
        #     i +=1
        #     j +=1
        #     print(x,y,eucledianGCD(x,y),LCD(x,y),nums)


        # return  [ n for n in nums if n > 0]     

#no se por que no funciona
#----------------------------------------------------------      


        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack







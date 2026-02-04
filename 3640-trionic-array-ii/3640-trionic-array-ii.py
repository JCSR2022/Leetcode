class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        # #aproach, create 3 stages, save sum of each stage..
        # def resetStages():
        #     return False,False,False,0,0,0

        # stage1,stage2,stage3,stg_1,stg_2,stg_3 = resetStages()

        # max_trionic = float("-inf")
        # prev = nums[0]

        # for n in nums[1:]:
        #     #print(prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic,end=",")

        #     if n == prev:
        #         if stage3:
        #             max_trionic = max(max_trionic,stg_1+stg_2+stg_3)
        #         stage1,stage2,stage3,stg_1,stg_2,stg_3 = resetStages()

        #     if n > prev:
        #         if stage3:
        #             stg_3 += n
        #             prev = n
        #             #print("1.3",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)
        #             continue

        #         if stage2:
        #             stage3 = True
        #             stg_3 = n
        #             prev = n
        #             max_trionic = max(max_trionic,stg_1+stg_2+stg_3)
        #             #print("1.2",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)
        #             continue
                
        #         if stage1:
        #             stg_1 += n
        #             prev = n
        #             #print("1.1",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)
        #             continue
                
        #         stage1 =True
        #         stg_1 = n+prev
            
        #     else:
        #         if stage3:
        #             max_trionic = max(max_trionic,stg_1+stg_2+stg_3)
        #             stage3 =False
        #             stg_1 = stg_3
        #             stg_2 = n
        #             prev = n
        #             #print("2.3",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)
        #             continue

        #         if stage2:
        #             stg_2 +=n
        #             prev = n
        #             #print("2.2",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)
        #             continue

        #         if stage1:
        #             stage2 = True
        #             stg_2 = n
                
        #     prev = n
        #     #print("#",prev,n,stage1,stage2,stage3,stg_1,stg_2,stg_3,max_trionic)

        # if stage3:
        #     max_trionic = max(max_trionic,stg_1+stg_2+stg_3)

        # return  max_trionic 

#vete a la mierda!!!!
#-------------------------------------------------------------


        # up1 = down = up2 = float("-inf")
        # res = float("-inf")

        # for i in range(1, len(nums)):
        #     diff = nums[i] - nums[i - 1]

        #     new_up1 = new_down = new_up2 = float("-inf")

        #     # --- primera subida ---
        #     if diff > 0:
        #         new_up1 = max(nums[i - 1] + nums[i], up1 + nums[i])

        #     # --- bajada ---
        #     if diff < 0 and up1 != float("-inf"):
        #         new_down = max(up1 + nums[i], down + nums[i])

        #     # --- segunda subida ---
        #     if diff > 0 and down != float("-inf"):
        #         new_up2 = max(down + nums[i], up2 + nums[i])

        #     up1 = max(up1, new_up1)
        #     down = max(down, new_down)
        #     up2 = max(up2, new_up2)

        #     res = max(res, up2)

        # return res

#----------------------------------------------------------------------

        #Suhrob 
        #??????????????????????????????????????????????

        n = len(nums)
        res = -float('inf')
        i = 1
        while i < n - 2:
            a = b = i
            net = nums[a]
            while b + 1 < n and nums[b + 1] < nums[b]:
                net += nums[b + 1]
                b += 1
            if b == a:
                i += 1
                continue
            
            c = b
            left = right = 0
            lx = rx = -float('inf')
            
            while a - 1 >= 0 and nums[a - 1] < nums[a]:
                left += nums[a - 1]
                lx = max(lx, left)
                a -= 1
            if a == i:
                i += 1
                continue
            
            while b + 1 < n and nums[b + 1] > nums[b]:
                right += nums[b + 1]
                rx = max(rx, right)
                b += 1
            if b == c:
                i += 1
                continue
                
            res = max(res, lx + rx + net)
            i = b
        return res if res != -float('inf') else 0












        
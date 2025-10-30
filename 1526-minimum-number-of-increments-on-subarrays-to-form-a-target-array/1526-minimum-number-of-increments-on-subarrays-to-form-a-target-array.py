class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        #brute force: n**3

        #find max target for i in range(len(target)) reapeat until max_targ:

        # size = len(target):
        # initial = [0]*size
        # max_target = max(target)
        # curr = 0

        # ans_count = 0
        # while curr < max_target:
        #     for i in range(size):
        #         if target[i] < initial[i]:
        #             initial[i] += 1
        #         else:
                

#noooooooooooooooooooooooooooooooooooooooooooooooooo
#-----------------------------------------------------------------

        # prev = 0
        # ans = 0
        # for num in target:
        #     if num > prev:
        #         ans += prev-num
        #     else:
        #         prev = num

        # return ans

#--------------------------------

        ans = target[0]

        for i in range(1,len(target)):
            if target[i] > target[i-1]:
                ans += target[i]-target[i-1]
            
        return ans





        




        
        
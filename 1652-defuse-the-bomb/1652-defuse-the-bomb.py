class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
#         new_code = code+code
        
#         if k > 0:
#             ans = [sum(new_code[i+1:i+1+k]) for i in range(len(code))]
#         elif k < 0:
#             ans = []
#             print(new_code)
#             for i in range(len(code)+1,0,-1):
#                 print(i,new_code[i+k:i],sum(new_code[i+k:i]))
#                 ans.append(sum(new_code[i+k:i]))
#             #ans = [sum(new_code[i+k:i]) for i in range(len(code),0,-1)]
#         else:
#             ans = [0]*len(code)
#         return ans 
    
    #---------------------
    
    #sliding window
    
    
        n=len(code)
        ans=[0]*n
        if k==0: return ans
        if k>0:
            ans[0]=wsum=sum(code[1:k+1])
            for l in range(1, n):
                r=(l+k)%n
                wsum+=-code[l]+code[r]
                ans[l]=wsum
            return ans
        # Python has minus index
        ans[0]=wsum=sum(code[-1:k-1:-1])
        for l in range(1, n):
            r=(l-k)%n
            wsum+=-code[-l]+code[-r]
            ans[-l]=wsum
        return ans
    
    
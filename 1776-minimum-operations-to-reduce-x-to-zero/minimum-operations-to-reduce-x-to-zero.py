class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:


        total_sum = sum(nums)
        target = total_sum - x
        
        # Si la suma total es exactamente x, quitamos todos los elementos
        if target == 0:
            return len(nums)
        # Si x es mayor que la suma de todo el arreglo, es imposible
        if target < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        # Ventana deslizable para encontrar el subarray central más largo
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Si nos pasamos del target, encogemos la ventana desde la izquierda
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Si encontramos la suma exacta, registramos el largo máximo
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # Si max_len cambió, la respuesta son los elementos que NO están en la ventana
        return len(nums) - max_len if max_len != -1 else -1


        # #maldito imbecil es una simple slideing window

        # size = len(nums)
        # total = sum(nums)
        # if total < x:
        #     return -1

        # target = total-x
        # l = 0 
        # r = 0
        # curr = 0
        # ans = float("inf")
        # while r < len(nums) and l <len(nums):
        #     curr += nums[r]
        #     if curr == target:
        #         ans = min(ans,total - (r-l))
        #         curr -= nums[l]
        #         l +=1
        #     if curr > target:
        #         l +=1

            
        # return ans if ans < float(inf) else -1 
 

        # #no puedes porque eres una madita basura!!!!!!



